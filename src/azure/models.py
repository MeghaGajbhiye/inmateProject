from django.db import models

# Create your models here.
class Azure(models.Model):
	subscription_id = models.CharField(max_length= 120, blank = True, null = True)
	client_id = models.CharField(max_length= 120, blank = True, null = True)
	secret_key = models.CharField(max_length=120, blank=True, null=True)
	tenant_id = models.CharField(max_length=120, blank=True, null=True)
	class Meta:
		# managed = False
		db_table = 'azure'
