def launch_instance(self, min_count, max_count, key_name, instance_type, monitoring):
>>>launch_instance(1, 1, megha, ubuntu server, enabled)
instance created
>>>launch_instance(2, 1, pushpa, linux server, enabled)
instance created
>>>launch_instance(2, 2, megha, windows server, disabled)
instance created
return(min_count, max_count, key_name, instance_type, monitoring)

def terminate_instance(self, instance_id):

>>>terminate_instance(123)
instance
>>>terminate_instance(2468)
instance terminated
>>>terminate_instance(6432)
instance terminated
return(instance_id)

