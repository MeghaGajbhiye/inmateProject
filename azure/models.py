from django.db import models

# Create your models here.
class Azure(models.Model):
	enrollment_number = models.CharField(max_length= 120, blank = True, null = True)
	api_key = models.CharField(max_length= 120, blank = True, null = True)
