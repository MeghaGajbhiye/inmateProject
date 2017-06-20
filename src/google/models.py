from django.db import models

class Google(models.Model):
	project_id = models.CharField(max_length= 120, blank = True, null = True)
	client_secret = models.CharField(max_length=120, blank=True, null=True)
	refresh_token = models.CharField(max_length=120, blank=True, null=True)
