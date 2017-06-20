import os
import datetime

# #3rd Party Libraries
from azure.mgmt.resource import ResourceManagementClient as rmc
from azure.monitor import MonitorClient as mc
from azure.common.credentials import ServicePrincipalCredentials as spc
from azure.mgmt.network import NetworkManagementClient as nmc
from azure.mgmt.storage import StorageManagementClient as smc
from azure.mgmt.compute import ComputeManagementClient as cmc
from haikunator import Haikunator as hk


class Azure_class:
    def __init__(self, sub_id, client_id, secret, tenant):

        self.haikunator = hk ()
        self.STORAGE_ACC_NAME = self.haikunator.haikunate (delimiter='')
        self.SUB_ID = sub_id            #Azure Subscription ID
        self.CLIENT_ID = client_id      #Azure Client ID
        self.TENANT_ID = tenant         #Azure Tenant ID
        self.SECRET_KEY = secret        #Azure Secret Key

        self.subscription_id = os.environ.get (
            'AZURE_SUBSCRIPTION_ID',
            self.SUB_ID)
        self.credentials = spc (
            client_id=self.CLIENT_ID,
            secret=self.SECRET_KEY,
            tenant=self.TENANT_ID
        )
        self.resource_client = rmc (self.credentials, self.subscription_id)
        self.compute_client = cmc (self.credentials, self.subscription_id)
        self.storage_client = smc (self.credentials, self.subscription_id)
        self.network_client = nmc (self.credentials, self.subscription_id)
        self.monitor_client = mc(self.credentials, self.subscription_id)

        self.VM_OS = {
            'linux': {
                'publisher': 'Canonical',
                'offer': 'UbuntuServer',
                'sku': '16.04.0-LTS',
                'version': 'latest'
            },
            'windows': {
                'publisher': 'MicrosoftWindowsServerEssentials',
                'offer': 'WindowsServerEssentials',
                'sku': 'WindowsServerEssentials',
                'version': 'latest'
            }
        }

    def create_resource_group(self, resource_group_name, location):
        """create resource group"""
        self.resource_client.resource_groups.create_or_update (resource_group_name, {'location': location})

    def create_storage_account(self, resource_group_name, location):
        """ Create a storage account """
        storage_async_operation = self.storage_client.storage_accounts.create (
            resource_group_name,
            self.STORAGE_ACC_NAME,
            {
                'sku': {'name': 'standard_lrs'},
                'kind': 'storage',
                'location': location
            }
        )
        storage_async_operation.wait ()

    def create_instance(self, choice, admin_username, admin_password, resource_group_name, vm_name, location,
                        vnet_name, subnet_name, nic_name, ip_config_name, os_disk_name):
        """Create instance"""
        self.create_resource_group (resource_group_name, location)
        self.create_storage_account (resource_group_name, location)
        self.create_vnet (self.network_client, resource_group_name, vnet_name, location)
        subnet_info = self.create_subnet (self.network_client, resource_group_name, vnet_name, subnet_name)
        nic = self.create_nic (self.network_client, subnet_info, resource_group_name, nic_name, location,
                               ip_config_name)

        if choice == 'linux':
            vm_params = self.create_parameters (nic.id, self.VM_OS['linux'], location, vm_name,
                                                admin_username, admin_password, os_disk_name)
            vm_creation = self.compute_client.virtual_machines.create_or_update (
                resource_group_name, vm_name, vm_params)
            vm_creation.wait ()

            vm_update = self.compute_client.virtual_machines.create_or_update (
                resource_group_name,
                vm_name,
                {
                    'location': location,
                    'tags': {
                        'who-rocks': 'python',
                        'where': 'on azure'
                    }
                }
            )
            vm_update.wait ()

            vm_update = self.compute_client.virtual_machines.create_or_update (
                resource_group_name,
                vm_name,
                {
                    'location': location,
                    'storage_profile': {
                        'data_disks': [{
                            'name': 'mydatadisk1',
                            'disk_size_gb': 1,
                            'lun': 0,
                            'vhd': {
                                'uri': "http://{}.blob.core.windows.net/vhds/mydatadisk1.vhd".format(
                                    self.STORAGE_ACC_NAME)
                            },
                            'create_option': 'Empty'
                        }]
                    }
                }
            )
            vm_update.wait ()

        elif self.choice == 'windows':
            vm_params = self.create_parameters (nic.id, self.VM_OS['windows'], location, vm_name,
                                                admin_username, admin_password, os_disk_name)
            vm_creation = self.compute_client.virtual_machines.create_or_update (
                resource_group_name, vm_name, vm_params)
            vm_creation.wait ()

    def update_instance(self, add_size, resource_group_name, vm_name):
        '''updating instance as per size'''
        virtual_machine = self.compute_client.virtual_machines.get (
            resource_group_name,
            vm_name
        )

        data_disks = virtual_machine.storage_profile.data_disks
        data_disks[:] = [disk for disk in data_disks if disk.name != 'mydatadisk1']
        async_vm_update = self.compute_client.virtual_machines.create_or_update (
            resource_group_name,
            vm_name,
            virtual_machine
        )
        virtual_machine = async_vm_update.result ()
        async_vm_deallocate = self.compute_client.virtual_machines.deallocate (resource_group_name, vm_name)
        async_vm_deallocate.wait ()
        if not virtual_machine.storage_profile.os_disk.disk_size_gb:
            virtual_machine.storage_profile.os_disk.disk_size_gb = 256

        virtual_machine.storage_profile.os_disk.disk_size_gb += add_size
        async_vm_update = self.compute_client.virtual_machines.create_or_update (
            resource_group_name,
            vm_name,
            virtual_machine
        )
        virtual_machine = async_vm_update.result ()

    def start_vm(self, resource_group_name, vm_name):
        '''start virtual machine'''
        async_vm_start = self.compute_client.virtual_machines.start (resource_group_name, vm_name)
        async_vm_start.wait ()

    def restart_vm(self, resource_group_name, vm_name):
        '''restart virtual machine'''
        async_vm_restart = self.compute_client.virtual_machines.restart (resource_group_name, vm_name)
        async_vm_restart.wait ()

    def stop_vm(self, resource_group_name, vm_name):
        '''stop virtual machine'''
        async_vm_stop = self.compute_client.virtual_machines.power_off (resource_group_name, vm_name)
        async_vm_stop.wait ()

    def view_instances_rgroup_name(self, resource_group_name):
        '''List VM in resource group'''
        vm_list = []
        for vm in self.compute_client.virtual_machines.list (resource_group_name):
            vm_list.append(vm.name)
        return vm_list

    def view_instances_sub(self):
        vm_list = []
        for vm in self.compute_client.virtual_machines.list_all ():
            vm_list.append(vm.name)
        return vm_list
            
    def delete_vm(self, resource_group_name, vm_name):
        '''delete virtual machine'''
        async_vm_delete = self.compute_client.virtual_machines.delete (resource_group_name, vm_name)
        async_vm_delete.wait()

    def delete_resource_group(self, resource_group_name):
        '''Delete Resource group and all it's resources'''
        delete_async_operation = self.resource_client.resource_groups.delete (resource_group_name)
        delete_async_operation.wait()
        
    def create_nic(self, network_client, subnet_info, resource_group_name, nic_name, location, ip_config_name):
        """Create a Network Interface for a VM."""
        async_nic_creation = network_client.network_interfaces.create_or_update (
            resource_group_name,
            nic_name,
            {
                'location': location,
                'ip_configurations': [{
                    'name': ip_config_name,
                    'subnet': {
                        'id': subnet_info.id
                    }
                }]
            }
        )
        return async_nic_creation.result ()

    def create_vnet(self, network_client, resource_group_name, vnet_name, location):
        '''to create virtual network'''
        async_vnet_creation = network_client.virtual_networks.create_or_update (
            resource_group_name,
            vnet_name,
            {
                'location': location,
                'address_space': {
                    'address_prefixes': ['10.0.0.0/16']
                }
            }
        )
        async_vnet_creation.wait ()

    def create_subnet(self, network_client, resource_group_name, vnet_name, subnet_name):
        # Create Subnet
        async_subnet_creation = network_client.subnets.create_or_update (
            resource_group_name,
            vnet_name,
            subnet_name,
            {'address_prefix': '10.0.0.0/24'}
        )
        subnet_info = async_subnet_creation.result ()
        return subnet_info

    def create_parameters(self, nic_id, vm_reference, location, vm_name, admin_username, admin_password,
                             os_disk_name):
        """Create the VM parameters structure."""
        return {
            'location': location,
            'os_profile': {
                'computer_name': vm_name,
                'admin_username': admin_username,
                'admin_password': admin_password
            },
            'hardware_profile': {
                'vm_size': 'Standard_DS1'
            },
            'storage_profile': {
                'image_reference': {
                    'publisher': vm_reference['publisher'],
                    'offer': vm_reference['offer'],
                    'sku': vm_reference['sku'],
                    'version': vm_reference['version']
                },
                'os_disk': {
                    'name': os_disk_name,
                    'caching': 'None',
                    'create_option': 'fromImage',
                    'vhd': {
                        'uri': 'https://{}.blob.core.windows.net/vhds/{}.vhd'.format (
                            self.STORAGE_ACC_NAME, vm_name + self.haikunator.haikunate ())
                    }
                },
            },
            'network_profile': {
                'network_interfaces': [{
                    'id': nic_id,
                }]
            },
        }

    def cloud_monitoring_metrics(self, resource_group_name, vm_name, parameter, days):
        ''' cloud monitoring steps'''
        resource_id = (
            "subscriptions/{}/"
            "resourceGroups/{}/"
            "providers/Microsoft.Compute/virtualMachines/{}"
        ).format (self.subscription_id, resource_group_name, vm_name)
        today = datetime.datetime.now ().date ()
        yesterday = today - datetime.timedelta (days=days)

        filter = " and ".join ([
            "name.value eq '{}'".format (parameter),
            "aggregationType eq 'Total'",
            "startTime eq {}".format (yesterday),
            "endTime eq {}".format (today),
            "timeGrain eq duration'PT1H'"
        ])

        metrics_data = self.monitor_client.metrics.list (
            resource_id,
            filter=filter
        )
        metric_list = []
        for item in metrics_data:
            for data in item.data:
                key_string = str(data.time_stamp)
                value_int = int(0 if data.total is None else data.total)
                metric_list.append([key_string, value_int])
        return metric_list

