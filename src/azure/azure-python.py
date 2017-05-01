import argparse
import os
import time
from azure.mgmt.resource import ResourceManagementClient as rmc
from azure.common.credentials import ServicePrincipalCredentials as spc
from azure.mgmt.network import NetworkManagementClient as nmc
from azure.mgmt.storage import StorageManagementClient as smc
from azure.mgmt.compute import ComputeManagementClient as cmc
from haikunator import Haikunator as hk


# things to ask user -subnet_name, vnet-name,group-name,location,
# ip-config-name, nic-name, username, password, vm-name, vm-type,


class Azure:
    def __init__(self, sub_id, client_id, secret, tenant):

        self.haikunator = hk ()
        self.STORAGE_ACC_NAME = self.haikunator.haikunate (delimiter='')
        self.SUB_ID = sub_id
        self.CLIENT_ID = client_id
        self.TENANT_ID = tenant
        self.SECRET_KEY = secret

        self.subscription_id = os.environ.get (
            'AZURE_SUBSCRIPTION_ID',
            self.SUB_ID)  # your Azure Subscription Id
        self.credentials = spc (
            client_id=self.CLIENT_ID,
            secret=self.SECRET_KEY,
            tenant=self.TENANT_ID
        )
        self.resource_client = rmc (self.credentials, self.subscription_id)
        self.compute_client = cmc (self.credentials, self.subscription_id)
        self.storage_client = smc (self.credentials, self.subscription_id)
        self.network_client = nmc (self.credentials, self.subscription_id)

        self.VM_REFERENCE = {
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


    # Create Resource group
    def create_resource_group(self, resource_group_name, location):
        """create resource group"""
        print('\nCreate Resource Group')
        self.resource_client.resource_groups.create_or_update (resource_group_name, {'location': location})

    def create_storage_account(self, resource_group_name, location):
        """ Create a storage account """
        print('\nCreate a storage account')
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
            # Create Linux VM
            print('\nCreating Linux Virtual Machine')
            vm_parameters = self.create_vm_parameters (nic.id, self.VM_REFERENCE['linux'], location, vm_name,
                                                       admin_username, admin_password, os_disk_name)
            async_vm_creation = self.compute_client.virtual_machines.create_or_update (
                resource_group_name, vm_name, vm_parameters)
            async_vm_creation.wait ()

            # Tag the VM
            print('\nTag Virtual Machine')
            async_vm_update = self.compute_client.virtual_machines.create_or_update (
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
            async_vm_update.wait ()

            # Attach data disk
            print('\nAttach Data Disk')
            async_vm_update = self.compute_client.virtual_machines.create_or_update (
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
            async_vm_update.wait ()

        elif self.choice == 'windows':
            # Create Windows VM
            print('\nCreating Windows Virtual Machine')
            vm_parameters = self.create_vm_parameters (nic.id, self.VM_REFERENCE['windows'], location, vm_name,
                                                       admin_username, admin_password, os_disk_name)
            async_vm_creation = self.compute_client.virtual_machines.create_or_update (
                resource_group_name, vm_name, vm_parameters)
            async_vm_creation.wait ()

    def update_instance(self, add_size, resource_group_name, vm_name):

        # Get one the virtual machine by name
        print('\nGet Virtual Machine by Name')
        virtual_machine = self.compute_client.virtual_machines.get (
            resource_group_name,
            vm_name
        )

        # Detach data disk
        print('\nDetach Data Disk')
        data_disks = virtual_machine.storage_profile.data_disks
        data_disks[:] = [disk for disk in data_disks if disk.name != 'mydatadisk1']
        async_vm_update = self.compute_client.virtual_machines.create_or_update (
            resource_group_name,
            vm_name,
            virtual_machine
        )
        virtual_machine = async_vm_update.result ()

        # Deallocating the VM (resize prepare)
        print('\nDeallocating the VM (resize prepare)')
        async_vm_deallocate = self.compute_client.virtual_machines.deallocate (resource_group_name, vm_name)
        async_vm_deallocate.wait ()

        print('\nUpdate OS disk size')
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
        print('\nStart VM')
        async_vm_start = self.compute_client.virtual_machines.start (resource_group_name, vm_name)
        async_vm_start.wait ()

    def restart_vm(self, resource_group_name, vm_name):
        print('\nRestart VM')
        async_vm_restart = self.compute_client.virtual_machines.restart (resource_group_name, vm_name)
        async_vm_restart.wait ()

    def stop_vm(self, resource_group_name, vm_name):
        print('\nStop VM')
        async_vm_stop = self.compute_client.virtual_machines.power_off (resource_group_name, vm_name)
        async_vm_stop.wait ()

    def view_instances(self, resource_group_name):
        print('\nList VMs in subscription')
        for vm in self.compute_client.virtual_machines.list_all ():
            print("\tVM: {}".format (vm.name))

        # List VM in resource group
        print('\nList VMs in resource group')
        for vm in self.compute_client.virtual_machines.list (resource_group_name):
            print("\tVM: {}".format (vm.name))

    def delete_vm(self, resource_group_name, vm_name):
        print('\nDelete VM')
        async_vm_delete = self.compute_client.virtual_machines.delete (resource_group_name, vm_name)
        async_vm_delete.wait()

    def delete_resource_group(self, resource_group_name):
        # Delete Resource group and everything in it
        print('\nDelete Resource Group')
        delete_async_operation = self.resource_client.resource_groups.delete (resource_group_name)
        delete_async_operation.wait()
        print("\nDeleted: {}".format(resource_group_name))

    def create_nic(self, network_client, subnet_info, resource_group_name, nic_name, location, ip_config_name):
        """Create a Network Interface for a VM."""

        print('\nCreate NIC')
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
        print('\nCreate Vnet')
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
        print('\nCreate Subnet')
        async_subnet_creation = network_client.subnets.create_or_update (
            resource_group_name,
            vnet_name,
            subnet_name,
            {'address_prefix': '10.0.0.0/24'}
        )
        subnet_info = async_subnet_creation.result ()
        return subnet_info

    def create_vm_parameters(self, nic_id, vm_reference, location, vm_name, admin_username, admin_password,
                             os_disk_name):
        """Create the VM parameters structure.
        """
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


if __name__ == "__main__":
    az = Azure('', '', '', '')
    # az.delete_resource_group("azure-sample-group-virtual-machines2")
    # az.start_vm("group1", "vm1")
    # az.restart_vm("group1", "vm1")
    # az.update_instance(10,"group1","vm1")
    # az.view_instances("group1")
    az.create_instance("linux", "megha", "MeghaRocks@1", "group1", "vm1", "westus", "vnet1", "subnet1", "nic1", "ipconfig1", "osdisk1")
