from django.test import TestCase

# Create your tests here.
def launch_instance(self, instance_name, image_name, ram):
>>>launch_instance(megha, Fedora 24(PVHVM), RAM: 512)
instance created
>>>launch_instance(pushpa, CentOS 6(PV), RAM: 1024)
instance created
>>>launch_instance(new, CentOS 7(PVHVM), RAM: 7680)
instance created
return(instance_name, image_name, ram)

def view-instances(self):
>>>view_instaces()
return(1)

def update_instances(self, server_name, ram):
>>>update_instances(Ubuntu server, RAM: 512)
instances updated
>>>update_instances(Linux server, RAM: 1024)
instances updated
>>>update_instances(Windows server, RAM: 7680)
instances updated
return(server_name, ram)

def delete_instances(self, server_name):
>>>delete_instances(Ubuntu server)
instances deleted
>>>delete_instances(Linux server)
instances deleted
>>>delete_instances(Windows server)
instances deleted
return(server_name, ram)

def instance_reboot(self, server_name, boot_type):
>>>instance_reboot(Ubuntu server, forced)
instance rebooted
>>>instance_reboot(Linux server, normal)
instance rebooted
>>>instance_reboot(Windows server, forced)
instance rebooted
return(server_name, boot_type)