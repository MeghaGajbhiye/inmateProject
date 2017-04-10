from django.db import models

# Create your models here.

class Rackspace(models.Model):
	tenant_id = models.CharField(max_length= 120, blank = True, null = True)