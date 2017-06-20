from django.db import models
from  django.contrib.auth.models import User
import boto

class AWSModel(models.Model):
    user_id = models.IntegerField(blank=False, primary_key=True)
    aws_access_key = models.CharField(max_length=120, blank=True, null=True)
    aws_secret_key = models.CharField(max_length=120, blank=True, null=True)
