import os
import datetime

# #3rd Party Libraries
# # from azure.mgmt.resource import ResourceManagementClient as rmc
# from azure.monitor import MonitorClient as mc
# from azure.common.credentials import ServicePrincipalCredentials as spc
# from azure.mgmt.network import NetworkManagementClient as nmc
# from azure.mgmt.storage import StorageManagementClient as smc
# from azure.mgmt.compute import ComputeManagementClient as cmc
# from haikunator import Haikunator as hk


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

        print "*****************************************inside create instance**********************************"
        print self.SUB_ID, self.CLIENT_ID, self.TENANT_ID, self.SECRET_KEY, choice, admin_username, admin_password, resource_group_name, vm_name, location, vnet_name
        subnet_name, nic_name, ip_config_name, os_disk_name
        # self.create_resource_group (resource_group_name, location)
        # self.create_storage_account (resource_group_name, location)
        # self.create_vnet (self.network_client, resource_group_name, vnet_name, location)
        # subnet_info = self.create_subnet (self.network_client, resource_group_name, vnet_name, subnet_name)
        # nic = self.create_nic (self.network_client, subnet_info, resource_group_name, nic_name, location,
        #                        ip_config_name)
        #
        # if choice == 'linux':
        #     # Launching Linux Virtual Machine
        #     vm_params = self.create_parameters (nic.id, self.VM_OS['linux'], location, vm_name,
        #                                         admin_username, admin_password, os_disk_name)
        #     vm_creation = self.compute_client.virtual_machines.create_or_update (
        #         resource_group_name, vm_name, vm_params)
        #     vm_creation.wait ()
        #
        #     # Tag the Virtual Machine
        #     vm_update = self.compute_client.virtual_machines.create_or_update (
        #         resource_group_name,
        #         vm_name,
        #         {
        #             'location': location,
        #             'tags': {
        #                 'who-rocks': 'python',
        #                 'where': 'on azure'
        #             }
        #         }
        #     )
        #     vm_update.wait ()
        #
        #     # Attach the data disk to virtual machine.
        #     vm_update = self.compute_client.virtual_machines.create_or_update (
        #         resource_group_name,
        #         vm_name,
        #         {
        #             'location': location,
        #             'storage_profile': {
        #                 'data_disks': [{
        #                     'name': 'mydatadisk1',
        #                     'disk_size_gb': 1,
        #                     'lun': 0,
        #                     'vhd': {
        #                         'uri': "http://{}.blob.core.windows.net/vhds/mydatadisk1.vhd".format(
        #                             self.STORAGE_ACC_NAME)
        #                     },
        #                     'create_option': 'Empty'
        #                 }]
        #             }
        #         }
        #     )
        #     vm_update.wait ()
        #
        # elif self.choice == 'windows':
        #     # Create Windows VM
        #     print('\nCreating Windows Virtual Machine')
        #     vm_params = self.create_parameters (nic.id, self.VM_OS['windows'], location, vm_name,
        #                                         admin_username, admin_password, os_disk_name)
        #     vm_creation = self.compute_client.virtual_machines.create_or_update (
        #         resource_group_name, vm_name, vm_params)
        #     vm_creation.wait ()

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

    def view_instances_rgroup_name(self, resource_group_name):
        '''List VM in resource group'''
        print('\nList VMs in resource group')
        for vm in self.compute_client.virtual_machines.list (resource_group_name):
            print("\tVM: {}".format (vm.name))

    def view_instances_sub(self):
        print('\nList VMs in subscription')
        for vm in self.compute_client.virtual_machines.list_all ():
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

    def create_parameters(self, nic_id, vm_reference, location, vm_name, admin_username, admin_password,
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

    def cloud_monitor(self):
        print "I am here"
        today = datetime.datetime.now ().date ()
        filter = " and ".join ([
            "eventTimestamp ge {}".format (today),
            "resourceGroupName eq 'ResourceGroupName'"
        ])
        select = ",".join ([
            "eventName",
            "operationName"
        ])

        activity_logs = self.monitor_client.activity_logs.list (
            filter=filter,
            select=select
        )
        print activity_logs

        for log in activity_logs:
            # assert isinstance(log, azure.monitor.models.EventData)
            print(" ".join ([
                log.event_name.localized_value,
                log.operation_name.localized_value
            ]))

#     def cloud_monitoring_metrics(self, resource_group_name, vm_name):
#         resource_id = (
#             "subscriptions/{}/"
#             "resourceGroups/{}/"
#             "providers/Microsoft.Compute/virtualMachines/{}"
#         ).format (self.subscription_id, resource_group_name, vm_name)
#
#         for metric in self.monitor_client.metric_definitions.list (resource_id):
#             print("{}: id={}, unit={}".format (
#                 metric.name.localized_value,
#                 metric.name.value,
#                 metric.unit
#             ))
#         #
#         # Percentage
#         # CPU: id = Percentage
#         # CPU, unit = Unit.percent
#         # Network
#         # In: id = Network
#         # In, unit = Unit.bytes
#         # Network
#         # Out: id = Network
#         # Out, unit = Unit.bytes
#         # Disk
#         # Read
#         # Bytes: id = Disk
#         # Read
#         # Bytes, unit = Unit.bytes
#         # Disk
#         # Write
#         # Bytes: id = Disk
#         # Write
#         # Bytes, unit = Unit.bytes
#         # Disk
#         # Read
#         # Operations / Sec: id = Disk
#         # Read
#         # Operations / Sec, unit = Unit.count_per_second
#         # Disk
#         # Write
#         # Operations / Sec: id = Disk
#         # Write
#         # Operations / Sec, unit = Unit.count_per_second
#
#         # Get CPU total of yesterday for this VM, by hour
#
#         today = datetime.datetime.now ().date ()
#         yesterday = today - datetime.timedelta (days=1)
#
#         filter = " and ".join ([
#             "name.value eq 'Percentage CPU'",
#             "aggregationType eq 'Total'",
#             "startTime eq {}".format (yesterday),
#             "endTime eq {}".format (today),
#             "timeGrain eq duration'PT1H'"
#         ])
#
#         metrics_data = self.monitor_client.metrics.list (
#             resource_id,
#             filter=filter
#         )
#
#         for item in metrics_data:
#             # azure.monitor.models.Metric
#             print("{} ({})".format (item.name.localized_value, item.unit.name))
#             for data in item.data:
#                 # azure.monitor.models.MetricData
#                 print("{}: {}".format (data.time_stamp, data.total))
#                 #
#                 # 2017 - 04 - 29
#                 # 00:00:00 + 00:00: None
#                 # 2017 - 04 - 29
#                 # 01:00:00 + 00:00: None
#                 # 2017 - 04 - 29
#                 # 02:00:00 + 00:00: None
#                 # 2017 - 04 - 29
#                 # 03:00:00 + 00:00: None
#                 # 2017 - 04 - 29
#                 # 04:00:00 + 00:00: None
#                 # 2017 - 04 - 29
#                 # 05:00:00 + 00:00: None
#                 # 2017 - 04 - 29
#                 # 06:00:00 + 00:00: None
#                 # 2017 - 04 - 29
#                 # 07:00:00 + 00:00: None
#                 # 2017 - 04 - 29
#                 # 0
#                 # 8:00:00 + 00:00: None
#                 # 2017 - 04 - 29
#                 # 0
#                 # 9:00:00 + 00:00: None
#                 # 2017 - 04 - 29
#                 # 10:00:00 + 00:00: None
#                 # 2017 - 04 - 29
#                 # 11:00:00 + 00:00: None
#                 # 2017 - 04 - 29
#                 # 12:00:00 + 00:00: None
#                 # 2017 - 04 - 29
#                 # 13:00:00 + 00:00: None
#                 # 2017 - 04 - 29
#                 # 14:00:00 + 00:00: None
#                 # 2017 - 04 - 29
#                 # 15:00:00 + 00:00: None
#                 # 2017 - 04 - 29
#                 # 16:00:00 + 00:00: None
#                 # 2017 - 04 - 29
#                 # 17:00:00 + 00:00: None
#                 # 2017 - 04 - 29
#                 # 18:00:00 + 00:00: None
#                 # 2017 - 04 - 29
#                 # 19:00:00 + 00:00: None
#                 # 2017 - 04 - 29
#                 # 20:00:00 + 00:00: None
#                 # 2017 - 04 - 29
#                 # 21:00:00 + 00:00: None
#                 # 2017 - 04 - 29
#                 # 22:00:00 + 00:00: None
#                 # 2017 - 04 - 29
#                 # 23:00:00 + 00:00: None
#
#     def azure_offers(self):
#         print "inside azure offers"
#         region = 'eastus2'
#         result_list_pub = self.compute_client.virtual_machine_images.list_publishers (region,)
#         for publisher in result_list_pub:
#             result_list_offers = self.compute_client.virtual_machine_images.list_offers(region, publisher.name,)
#             for offer in result_list_offers:
#                 result_list_skus = self.compute_client.virtual_machine_images.list_skus (region, publisher.name,offer.name,)
#                 for sku in result_list_skus:
#                     result_list = self.compute_client.virtual_machine_images.list(region,publisher.name,offer.name,sku.name,)
#                     for version in result_list:
#                         result_get = self.compute_client.virtual_machine_images.get (region,publisher.name,offer.name,sku.name,version.name,)
#                         print('PUBLISHER: {0}, OFFER: {1}, SKU: {2}, VERSION: {3}'.format (publisher.name,offer.name,sku.name,version.name,))
#
#
#     def create_snapshot(self, resource_group_name, disk_name):
#         managed_disk = self.compute_client.disks.get (resource_group_name, disk_name)
#         async_snapshot_creation = self.compute_client.snapshots.create_or_update (
#             'my_resource_group',
#             'mySnapshot',
#             {
#                 'location': 'westus',
#                 'creation_data': {
#                     'create_option': 'Copy',
#                     'source_uri': managed_disk.id
#                 }
#             }
#         )
#         snapshot = async_snapshot_creation.result ()
#
# if __name__ == "__main__":
#     az = Azure_class('7197d513-b8a1-425e-9065-2cf1cb785455', 'ad6f5554-f2ae-420d-af5d-831cdc7ce984', 'F5bL1mmVolS999DO8mxoLhqQa8te3Pge5JQF8T70YLo=', '98eccb32-1911-4822-a103-1d2a2db59a9e')
#     # az.create_snapshot("group1", "osdisk1")
#     # az.azure_offers()
#     # az.cloud_monitor()
#     # az.cloud_monitoring_metrics("group1","vm1")
#     # az.delete_resource_group("azure-sample-group-virtual-machines2")
#     # az.start_vm("group1", "vm1")
#     # az.restart_vm("group1", "vm1")
#     # az.update_instance(10,"group1","vm1")
#     az.view_instances_rgroup_name("group1")
#     az.view_instances_sub()
#     # az.create_instance("linux", "megha", "MeghaRocks@1", "group1", "vm1", "westus", "vnet1", "subnet1", "nic1", "ipconfig1", "osdisk1")
