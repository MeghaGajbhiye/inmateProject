from django.conf import settings
import boto
aws_access_key_id = 'AKIAJKLGF55A33R3KTMQ'
aws_secret_access_key = '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'
ec2 = boto.connect_ec2(aws_access_key_id=aws_access_key_id,
aws_secret_access_key=aws_secret_access_key)

#checking all zones
# print ec2.get_all_zones()
print  boto.ec2.regions()

 

#checking all regions  
# print  boto.ec2.regions()
eu_conn = boto.ec2.connect_to_region('eu-west-1', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)

# boto.set_stream_logger('paws')
# ec2 = boto.connect_ec2(debug=2)
# s3 = boto.connect_s3(debug=2)
#
# instances = ec2.instances.filter(
#     Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])
# for instance in instances:
#     print(instance.id, instance.instance_type)

