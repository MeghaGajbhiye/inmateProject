from django.db import models

# Create your models here.
class Google(models.Model):
	project_id = models.CharField(max_length= 120, blank = True, null = True)