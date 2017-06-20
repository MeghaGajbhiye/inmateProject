from django.db import models

class Rackspace(models.Model):
	username = models.CharField(max_length= 120, blank = True, null = True)
	api_key = models.CharField(max_length= 120, blank = True, null = True)
