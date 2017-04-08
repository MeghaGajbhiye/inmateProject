from django.db import models
from django.conf import settings
from  django.contrib.auth.models import User

class AWS(models.Model):
    user = models.ForeignKey(User, default = '')
    aws_access_key = models.CharField(max_length=120, blank=True, null=True)
    aws_secret_key = models.CharField(max_length=120, blank=True, null=True)
    account_id = models.CharField(max_length=120, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'aws'

    # class AWSHome(models.Model):
    # 	aws_zone = models.CharField(max_length= 120, blank = True, null = True)
    # def __init__(self, *args, **kwargs):
    # 	super(AWSHome, self).__init__(*args, **kwargs)
    # 	self.fields['aws_zone'] = models.ChoiceField(choices = get_zone())

# Create your models here.
