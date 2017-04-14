import types

class AWS:

    def __init__(self, ak, sk, func=None):
        self.access_key = ak
        self.secret_key = sk
        if func is not None:
            self.execute = func

    def execute(self):
        print("AWS")

    def get_acccess_key(self):
        return self.access_key

    def get_secret_key(self):
        return self.secret_key

    # def cloudwatchmonitoring:


    def describe_instances(self):
        ec2 = boto3.client('ec2', aws_access_key_id=getAccessKey(), aws_secret_access_key=getSecretKey())
        ec2_out = ec2.describe_instances()
        for reservation in ec2_out['Reservations']:
            reservation_id = reservation['ReservationId']
            instance_id = reservation['Instances'][0]['InstanceId']
            print (reservation_id, instance_id)

    def launch_instance(self):
        ec2 = boto3.client('ec2', aws_access_key_id=getAccessKey(),
                           aws_secret_access_key=getSecretKey())
        ec2_out = ec2.run_instances(ImageId='ami-8ca83fec', MinCount=1, MaxCount=1, KeyName='ravi',
                                    InstanceType='m4.xlarge', Monitoring={'Enabled': True})
        print (ec2_out)

    # http://boto3.readthedocs.io/en/latest/reference/services/ec2.html#EC2.Client.run_instances


    def describe_security_groups(self):
        ec2 = boto3.client('ec2', aws_access_key_id=getAccessKey(),
                           aws_secret_access_key=getSecretKey())
        ec2_out = ec2.describe_security_groups()
        for security_group in ec2_out['SecurityGroups']:
            print (security_group['GroupName'])

    def describe_subnets(self):
        ec2 = boto3.client('ec2', aws_access_key_id=getAccessKey(),
                           aws_secret_access_key=getSecretKey())
        ec2_out = ec2.describe_subnets()
        for subnet in ec2_out['Subnets']:
            print (subnet['SubnetId'])

    def describe_images(self):
        ec2 = boto3.client('ec2', aws_access_key_id=getAccessKey(),
                           aws_secret_access_key=getSecretKey())
        ec2_out = ec2.describe_images()
        for image in ec2_out['Images']:
            image_id = image['ImageId']
            # image_os = image['Name']
            print (image_id, image_os)