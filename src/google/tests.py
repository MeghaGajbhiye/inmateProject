from django.test import TestCase

# Create your tests here.
def create_instance(self, project_id, zone, instance_name, bucket_name):
>>>create_instance(123, virginia, megha, megha)
instance created
>>>create_instance(2367, dallas, pushpa, pushpa)
instance created
>>>create_instance(6589, virginia, new, new)
instance created
return(project_id, zone, instance_name, bucket_name)

def list_instances(self, project_id, zone):
>>>list_instance(123, virginia)
instances listed
>>>list_instance(2367, dallas)
instances listed
>>>list_instance(6589, virginia)
instances listed
return(project_id, zone)

def delete_instance(self, project_id, instance_name):
>>>delete_instance(123, megha)
instance deleted
>>>delete_instance(2367, pushpa)
instance deleted
>>>delete_instance(6589, new)
instance deleted
return(project_id, instance_name)
