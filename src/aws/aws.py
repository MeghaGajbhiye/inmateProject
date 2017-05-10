import types
import boto3
from datetime import datetime, timedelta
 
class AWS:

    def __init__(self, ak, sk):
        self.access_key = ak
        self.secret_key = sk

    def get_acccess_key(self):
        return self.access_key
        #return self.access_key

    def get_secret_key(self):
        return self.secret_key
        #return self.secret_key

    def describe_instances(self, region_name):
        print "*******************************inside describe images***********************************************"
        print self.secret_key, self.access_key
        print ('Inside describe method')
        ec2 = boto3.client('ec2',aws_access_key_id=self.get_acccess_key(),aws_secret_access_key=self.get_secret_key(), region_name=region_name)
        next_token=''
        ec2_out = ec2.describe_instances(Filters=[{
		'Name':'instance-state-name',
		'Values':[
		'running'
		]}],
		NextToken=next_token)
        list_instanceid = []
        for reservation in ec2_out['Reservations']:
            instance_id = reservation['Instances'][0]['InstanceId']
            print str(instance_id)
            list_instanceid.append(instance_id)
        return list_instanceid

    def describe_key_pair(self):
        ec2 = boto3.client('ec2',aws_access_key_id=self.get_acccess_key(),aws_secret_access_key=self.get_secret_key())
        ec2_out = ec2.describe_key_pairs()
        print ec2_out

    def launch_instance(self,image_id, region_name, min_count, max_count, key_name, instance_type,monitoring):
        print "*******************************inside launch instance *************************************"
        print self.secret_key, self.access_key, min_count, max_count, key_name, instance_type, monitoring

        print "I am inside launch instance"
        ec2 = boto3.client('ec2', aws_access_key_id=self.get_acccess_key(),
                           aws_secret_access_key=self.get_secret_key(), region_name = region_name)
        image_id = 'ami-8ca83fec'
        #self.describe_images()
        # ec2_out = ec2.run_instances(ImageId='ami-8ca83fec', MinCount=1, MaxCount=1, KeyName='ravi',
        #                             InstanceType='m4.xlarge', Monitoring={'Enabled': True})


        ec2_out = ec2.run_instances(ImageId=image_id, MinCount=min_count, MaxCount=max_count, KeyName=key_name,
                                    InstanceType=instance_type, Monitoring={'Enabled': monitoring})
        print (ec2_out)

    # http://boto3.readthedocs.io/en/latest/reference/services/ec2.html#EC2.Client.run_instances

    def describe_security_groups(self):
        ec2 = boto3.client('ec2', aws_access_key_id=self.get_acccess_key(),
                           aws_secret_access_key=self.get_secret_key())
        ec2_out = ec2.describe_security_groups()
        for security_group in ec2_out['SecurityGroups']:
            return (security_group['GroupName'])

    def describe_subnets(self):
        ec2 = boto3.client('ec2', aws_access_key_id=self.get_acccess_key(),
                           aws_secret_access_key=self.get_secret_key())
        ec2_out = ec2.describe_subnets()
        for subnet in ec2_out['Subnets']:
            return (subnet['SubnetId'])

    def describe_images(self):
        ec2 = boto3.client('ec2', aws_access_key_id=self.get_acccess_key(),
                           aws_secret_access_key=self.get_secret_key())
        ec2_out = ec2.describe_images()
        for image in ec2_out['Images']:
            image_id = image['ImageId']
            # image_os = image['Name']
            return image_id
            # print (image_id, image_os)

    def terminate_instance(self, instance_id):
        print "***********************************inside terminate instance****************************************"
        print self.access_key, self.secret_key, instance_ids
        # ec2 = boto3.client ('ec2', aws_access_key_id=self.get_acccess_key(),
        #                     aws_secret_access_key=self.get_secret_key())
        # ec2_out = ec2.terminate_instances (InstanceIds=[instance_id])
        # print (ec2_out)

    def get_metrics(self, instance_ids):
        print "*****************************inside get metrics*************************************"
        print self.access_key, self.secret_key, instance_ids
        client = boto3.client('cloudwatch', aws_access_key_id=self.get_acccess_key(),
                            aws_secret_access_key=self.get_secret_key(), region_name=self.get_region_name())
        now = datetime.utcnow()
        start = now - timedelta(hours=3)

        metric_response = {}
        response =  client.get_metric_statistics(Namespace='AWS/EC2', MetricName=metric_name, Dimensions=[{'Name': 'InstanceId', 'Value': instance_id },], StartTime=start,EndTime=now, Period=120, Statistics=[ 'Average'])
        print (response['Label'])
        for datapoint in response['Datapoints']:
            metric_response[datapoint['Timestamp']] = datapoint['Average']
        metric_response_sorted = {}
        for metric_key in sorted(metric_response.keys()):
            metric_response_sorted[metric_key] = metric_response[metric_key]
        return metric_response_sorted
        # client = boto3.client('cloudwatch', aws_access_key_id=self.get_acccess_key(),
        #                     aws_secret_access_key=self.get_secret_key())
        # now = datetime.utcnow()
        # start = now - timedelta(hours=3)
        # all_metrics = ['CPUUtilization','DiskReadOps','DiskWriteOps', 'DiskReadBytes', 'DiskWriteBytes','NetworkIn',
        # 'NetworkOut','NetworkPacketsIn','NetworkPacketsOut','StatusCheckFailed']
        # for metric in all_metrics:
        #     response =  client.get_metric_statistics(
        #         Namespace='AWS/EC2',
        #         MetricName="CPUUtilization",
        #         Dimensions=[{'Name': 'InstanceId','Value': 'i-0cae18706985f552e'},],
        #         StartTime=start,
        #         EndTime=now,
        #         Period=120,
        #         Statistics=['Average'])
        # print (response)
    
# def cloudwatchmonitoring(self):
    #     print "I am inside cloudwatch"
    #     instance_id_list  = self.describe_instances()
    #     now = datetime.utcnow()
    #     past = now - timedelta(minutes=30)
    #     future = now + timedelta(minutes=10)
    #     print ("size of instances = " + instance_id_list.len)
    #     cw_client = boto3.client('CloudWatch', aws_access_key_id=self.get_acccess_key(), aws_secret_access_key=self.get_secret_key())
    #     for instance_id in instance_id_list:
    #         cw_out = cw_client.get_metric_statistics(
    #             NameSpace='AWS/EC2',
    #             MetricName='CPUUtilization',
    #             Dimensions=[{'Name': 'InstanceId', 'Value': instance_id}],
    #             StartTime=past,
    #             EndTime=future,
    #             Period=300,
    #             Statistics=['Average']
    #         )
    #         print (cw_out)




if __name__ == "__main__":
    # aws_access_key_id = '', aws_secret_access_key = 'ZOcCCejDCDWLoMNhzpr0R+YJQvr0n2mvwHAhy9zy'
    aws = AWS("AKIAIR6NSMV54GLQET2A", "Z51MMk4s0eyeWPyaS2jMi0XMlIkZ7BJTZAtZ3tY+")
    instances = aws.describe_instances("us-west-2")
    # aws.describe_key_pair()
    # for instance in instances:
    #     print (instance)
    #     aws.get_metrics(instance)
    #aws.launch_instance( 1, 1,'keypair2', 'c3.xlarge',True)
