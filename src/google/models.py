from django.db import models

# Create your models here.
class Google(models.Model):
	# user = models.ForeignKey('RegistrationRegistrationprofile', unique=True)
	project_id = models.CharField(max_length= 120, blank = True, null = True)
	# class Meta:
	# 	# managed = True
	# 	db_table = 'google'