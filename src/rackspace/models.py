from django.db import models

# Create your models here.

class Rackspace(models.Model):
	username = models.CharField(max_length= 120, blank = True, null = True)
	api_key = models.CharField(max_length= 120, blank = True, null = True)
	# class Meta:
	# 	# managed = False
	# 	db_table = 'rackspace'
