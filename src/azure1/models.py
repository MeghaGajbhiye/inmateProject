from django.db import models
class Azure(models.Model):
	subscription_id = models.CharField(max_length= 120, blank = True, null = True)
	client_id = models.CharField(max_length= 120, blank = True, null = True)
	secret_key = models.CharField(max_length=120, blank=True, null=True)
	tenant_id = models.CharField(max_length=120, blank=True, null=True)
	