from django.db import models

# Create your models here.
class IBM(models.Model):
	api_key = models.CharField(max_length= 120, blank = True, null = True)
