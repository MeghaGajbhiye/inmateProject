from django.db import models
from  django.contrib.auth.models import User

class ORACLEModel(models.Model):
    user_id = models.IntegerField(blank=False, primary_key=True)
    oracle_name = models.CharField(max_length=120, blank=True, null=True)
    oracle_password = models.CharField(max_length=120, blank=True, null=True)
    oracle_domain_name = models.CharField(max_length=120, blank=True, null=True)
