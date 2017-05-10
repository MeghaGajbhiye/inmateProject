from django.test import TestCase

# Create your tests here.
# def create_instance(self, choice, admin_username, admin_password, resource_group_name, vm_name, location, vnet_name, subnet_name, ip_config_name, OS_disk_name):
# """
# >>>create_instance(1, megha, 123, megha, windows server, virginia, C123, D264, Ceilo,  windowsxp)
# instace created
# >>>create_instance(2, pushpa, 611, pushpa, ubuntu server, virginia, C123, D264, Ceilo, ubuntu7.0)
# instace created
# >>>create_instance(1, new, 643, new, linux server, dallas, C124, B681, Dumb2,  redhat)
# instace created
# """
# return (choice, admin_username, admin_password, resource_group_name, vm_name, location, vnet_name, subnet_name, ip_config_name, OS_disk_name)
#
# def update_instance(self, add_size, resource_group_name, vm_name):
# """
# >>>update_instance(small(6GB), megha, windows server)
# instance updated
# >>>update_instance(medium(8GB), pushpa, ubuntu server)
# instance updated
# >>>update_instance(small(6GB), new, linux server)
# instance updated
# """
# return(add_size, resource_group_name, vm_name)
#
# def start_vm(self, resource_group_name, vm_name):
# """"
# >>>start_vm(megha, windows server)
# vm started
# >>>start_vm(pushpa, ubuntu server)
# vm started
# >>>start_vm(new, linux server)
# vm started
# """
# return(resource_group_name, vm_name)
#
# def restart_vm(self, resource_group_name, vm_name):
# """"
# >>>restart_vm(megha, windows server)
# vm restarted
# >>>restart_vm(pushpa, ubuntu server)
# vm restarted
# >>>restart_vm(new, linux server)
# vm restarted
# """
# return(resource_group_name, vm_name)
#
# def stop_vm(self, resource_group_name, vm_name):
# """"
# >>>stop_vm(megha, windows server)
# vm stopped
# >>>stop_vm(pushpa, ubuntu server)
# vm stopped
# >>>stop_vm(new, linux server)
# vm stopped
# """
# return(resource_group_name, vm_name)
#
# def view_instances(self, resource_group_name):
# """"
# >>>stop_vm(megha)
# instances viewed
# >>>stop_vm(pushpa)
# instances viewed
# >>>stop_vm(new)
# instances viewed
# """
# return(resource_group_name)
#
# def delete_vm(self, resource_group_name, vm_name):
# """"
# >>>delete_vm(megha, windows server)
# vm deleted
# >>>delete_vm(pushpa, ubuntu server)
# vm deleted
# >>>delete_vm(new, linux server)
# vm deleted
# """
# return(resource_group_name, vm_name)