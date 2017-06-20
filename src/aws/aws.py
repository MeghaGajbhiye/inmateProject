import types
import boto3
from datetime import datetime, timedelta
 
class AWS:

    def __init__(self, ak, sk, service):
        self.access_key = ak
        self.secret_key = sk
        self.service = service

    def get_acccess_key(self):
        return self.access_key
        #return self.access_key

    def get_secret_key(self):
        return self.secret_key
        #return self.secret_key

    def describe_instances(self, region_name):
        '''Show instances'''
        ec2 = boto3.client(self.service,aws_access_key_id=self.access_key,aws_secret_access_key=self.secret_key, region_name=region_name)
        ec2_out = ec2.describe_instances(Filters=[{
		'Name':'instance-state-name',
		'Values':[
		'running'
		]}])
        list_instanceid = []
        for reservation in ec2_out['Reservations']:
            instance_id = reservation['Instances'][0]['InstanceId']
            list_instanceid.append(str(instance_id))
        return list_instanceid

    def describe_key_pair(self):
        '''gets keypair'''
        ec2 = boto3.client(self.service,aws_access_key_id=self.get_acccess_key(),aws_secret_access_key=self.get_secret_key())
        ec2_out = ec2.describe_key_pairs()
        return   ec2_out

    def launch_instance(self, instance_name, region_name, image_id, instance_type, min_count, max_count, key_name, monitoring):
        '''to launch instance'''
        ec2 = boto3.client(self.service, aws_access_key_id=self.get_acccess_key(),
                           aws_secret_access_key=self.get_secret_key(), region_name = region_name)
        ec2_out = ec2.run_instances(ImageId=image_id, MinCount=min_count, MaxCount=max_count, KeyName=key_name,
                                    InstanceType=instance_type, Monitoring={'Enabled': monitoring},
                                    TagSpecifications=[{'ResourceType': 'instance','Tags': [{'Key': 'Name','Value': instance_name}]}])
        return (ec2_out)

    def describe_security_groups(self):
        '''to get security group'''
        ec2 = boto3.client(self.service, aws_access_key_id=self.get_acccess_key(),
                           aws_secret_access_key=self.get_secret_key())
        ec2_out = ec2.describe_security_groups()
        for security_group in ec2_out['SecurityGroups']:
            return (security_group['GroupName'])

    def describe_subnets(self):
        '''to get subnet'''
        ec2 = boto3.client(self.service, aws_access_key_id=self.get_acccess_key(),
                           aws_secret_access_key=self.get_secret_key())
        ec2_out = ec2.describe_subnets()
        for subnet in ec2_out['Subnets']:
            return (subnet['SubnetId'])

    def describe_images(self):
        '''to get images'''
        ec2 = boto3.client(self.service, aws_access_key_id=self.get_acccess_key(),
                           aws_secret_access_key=self.get_secret_key())
        ec2_out = ec2.describe_images()
        for image in ec2_out['Images']:
            image_id = image['ImageId']
            return image_id

    def terminate_instance(self, instance_id, region_name):
        ''' delete instances'''
        ec2 = boto3.client (self.service, aws_access_key_id=self.get_acccess_key(),
                            aws_secret_access_key=self.get_secret_key(), region_name = region_name)
        ec2_out = ec2.terminate_instances (InstanceIds=[instance_id])
        return (ec2_out)

    def get_metrics(self, instance_id, region_name, hours, parameter):
        '''monitoring parameters'''
        client = boto3.client(self.service, aws_access_key_id=self.get_acccess_key(),
                            aws_secret_access_key=self.get_secret_key(), region_name=region_name)
        now = datetime.utcnow()
        start = now - timedelta(hours=hours)

        metric_response = {}
        response =  client.get_metric_statistics(Namespace='AWS/EC2', MetricName=parameter,
                                                 Dimensions=[{'Name': 'InstanceId', 'Value': instance_id},],
                                                 StartTime=start,EndTime=now, Period=120, Statistics=[ 'Average'])
        for datapoint in response['Datapoints']:
            metric_response[datapoint['Timestamp']] = datapoint['Average']
        metric_response_sorted = {}
        for metric_key in sorted(metric_response.keys()):
            metric_response_sorted[metric_key] = metric_response[metric_key]

        monitor_list = []
        for date_value in metric_response_sorted:
            date_value_string = str(date_value)
            monitor_list.append([date_value_string, int(metric_response_sorted[date_value])])
        return monitor_list
       