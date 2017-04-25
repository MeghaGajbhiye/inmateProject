from django.db import models
from  django.contrib.auth.models import User
import boto

#
# def get_zone():
#     aws_access_key_id = 'AKIAJNGZXVEALHZW7P7A'
#     aws_secret_access_key = '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'
#     ec2 = boto.connect_ec2(aws_access_key_id=aws_access_key_id,
#                            aws_secret_access_key=aws_secret_access_key)
#     data = list(ec2.get_all_zones())
#     return data


class AWS(models.Model):
    #
    # user = User.objects.get(id = user_id)
    # print ("User is %r" %(User))
    user_id = models.IntegerField(blank=False, primary_key=True)
    aws_access_key = models.CharField(max_length=120, blank=True, null=True)
    aws_secret_key = models.CharField(max_length=120, blank=True, null=True)
    # account_id = models.CharField(max_length=120, blank=True, null=True)

    class Meta:
        # managed = True
        db_table = 'aws'


# class AWSHome(models.Model):
#     def __init__(self, *args, **kwargs):
#         super(AWSHome, self).__init__(*args, **kwargs)
#         self.fields['aws_zone'] = models.ChoiceField(choices=get_zone())

# Create your models here.
