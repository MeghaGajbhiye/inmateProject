from django.conf import settings
import boto
aws_access_key_id = 'AKIAI6ISOQQD66FZ7EPQ'
aws_secret_access_key = '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'
ec2 = boto.connect_ec2(aws_access_key_id=aws_access_key_id,
aws_secret_access_key=aws_secret_access_key)

#checking all zones
print ec2.get_all_zones() 

#checking all regioins  
print  boto.ec2.regions()
eu_conn = boto.ec2.connect_to_region('eu-west-1', aws_access_key_id=aws_access_key_id,
aws_secret_access_key=aws_secret_access_key)

boto.set_stream_logger('paws')
ec2 = boto.connect_ec2(debug=2)
s3 = boto.connect_s3(debug=2)


