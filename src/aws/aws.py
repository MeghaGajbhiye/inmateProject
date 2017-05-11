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
        print "*******************************inside describe images through region***********************************************"
        print (self.secret_key, type(self.secret_key), self.access_key, type(self.access_key), region_name, type(region_name))
        print ('Inside describe method')
        ec2 = boto3.client('ec2',aws_access_key_id=self.access_key,aws_secret_access_key=self.secret_key, region_name=region_name)
        print "authentication done"
        # next_token=''
        ec2_out = ec2.describe_instances(Filters=[{
		'Name':'instance-state-name',
		'Values':[
		'running'
		]}])
         #    ,
		# NextToken=next_token)
        list_instanceid = []
        print "inside list instances", list_instanceid
        for reservation in ec2_out['Reservations']:
            instance_id = reservation['Instances'][0]['InstanceId']
            list_instanceid.append(str(instance_id))
        print "list is", list_instanceid, type, type(list_instanceid)
        return list_instanceid

    def describe_key_pair(self):
        ec2 = boto3.client('ec2',aws_access_key_id=self.get_acccess_key(),aws_secret_access_key=self.get_secret_key())
        ec2_out = ec2.describe_key_pairs()
        print ec2_out

    def launch_instance(self, instance_name, region_name, image_id, instance_type, min_count, max_count, key_name, monitoring):
        print "*******************************inside launch instance *************************************"
        print self.secret_key, type(self.secret_key), self.access_key, type(self.access_key), \
            min_count, type(min_count), max_count, type(max_count), image_id, type(image_id), key_name, type(key_name), \
            instance_type, type(instance_type), monitoring, type(monitoring), region_name, type(region_name)

        print "I am inside launch instance"
        ec2 = boto3.client('ec2', aws_access_key_id=self.get_acccess_key(),
                           aws_secret_access_key=self.get_secret_key(), region_name = region_name)
        print "authentication done"
        # image_id = 'ami-8ca83fec'
        #self.describe_images()
        # ec2_out = ec2.run_instances(ImageId='ami-8ca83fec', MinCount=1, MaxCount=1, KeyName='ravi',
        #                             InstanceType='m4.xlarge', Monitoring={'Enabled': True})
        ec2_out = ec2.run_instances(ImageId=image_id, MinCount=min_count, MaxCount=max_count, KeyName=key_name,
                                    InstanceType=instance_type, Monitoring={'Enabled': monitoring},
                                    TagSpecifications=[{'ResourceType': 'instance','Tags': [{'Key': 'Name','Value': instance_name}]}])
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

    def terminate_instance(self, instance_id, region_name):
        print "***********************************inside terminate instance****************************************"
        print self.access_key, self.secret_key, instance_id, region_name, type(instance_id), type(region_name)
        ec2 = boto3.client ('ec2', aws_access_key_id=self.get_acccess_key(),
                            aws_secret_access_key=self.get_secret_key(), region_name = region_name)
        ec2_out = ec2.terminate_instances (InstanceIds=[instance_id])
        print (ec2_out)

    def get_metrics(self, instance_id, region_name, hours, parameter):
        print "*****************************inside get metrics*************************************"
        print self.access_key, type(self.access_key), self.secret_key, type(self.secret_key), \
            instance_id, type(instance_id), region_name, type(region_name), hours, type(hours), parameter, type(parameter)
        client = boto3.client('cloudwatch', aws_access_key_id=self.get_acccess_key(),
                            aws_secret_access_key=self.get_secret_key(), region_name=region_name)
        now = datetime.utcnow()
        start = now - timedelta(hours=hours)

        metric_response = {}
        response =  client.get_metric_statistics(Namespace='AWS/EC2', MetricName=parameter,
                                                 Dimensions=[{'Name': 'InstanceId', 'Value': instance_id},],
                                                 StartTime=start,EndTime=now, Period=120, Statistics=[ 'Average'])
        # print (response)
        for datapoint in response['Datapoints']:
            metric_response[datapoint['Timestamp']] = datapoint['Average']
        metric_response_sorted = {}
        for metric_key in sorted(metric_response.keys()):
            metric_response_sorted[metric_key] = metric_response[metric_key]
        # print metric_response_sorted

        monitor_list = []
        for date_value in metric_response_sorted:
            date_value_string = str(date_value)
            monitor_list.append([date_value_string, int(metric_response_sorted[date_value])])
            print type(metric_response_sorted[date_value])
        print monitor_list
        return monitor_list
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
    # aws = AWS("AKIAJWEDCTRMZZBKW54Q", "EOa6Wbhw3KWzfJtHij4iqbiKXJE6lOr7H+AMtX0Y")
    aws = AWS("AKIAJRWWW54B3HUPMQIA", "M6B4Z4fb3XT5WUW3l+6xfBOQTWFttXLibjtJCTnv")
    # instances = aws.describe_instances("us-west-2")
    # aws.describe_key_pair()
    # for instance in instances:
    #     print (instance)
    #     aws.get_metrics(instance)
    # aws.launch_instance( "instance_Console", "us-west-2", "ami-4836a428","t2.micro", 1, 1,'keypair2',True)
    # aws.terminate_instance("i-0f8cd205ff577869e", "us-west-2")
    aws.get_metrics("i-0cae18706985f552e", "us-west-2", 1, "CPUUtilization")