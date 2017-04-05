from django.db import models

# Create your models here.

class SignUp(models.Model):
	email = models.EmailField()
	full_name = models.CharField(max_length= 120, blank = True, null = True)
	timestamp = models.DateTimeField(auto_now_add = True, auto_now = False)
	updated= models.DateTimeField(auto_now_add= False, auto_now = True)
	password = models.CharField(max_length = 100)

	def __unicode__(self): 
		return self.email


class AWS(models.Model):
	aws_access_key = models.CharField(max_length= 120, blank = True, null = True)
	aws_secret_key = models.CharField(max_length= 120, blank = True, null = True)
	account_id = models.CharField(max_length= 120, blank = True, null = True)

class Azure(models.Model):
	enrollment_number = models.CharField(max_length= 120, blank = True, null = True)
	api_key = models.CharField(max_length= 120, blank = True, null = True)

class Google(models.Model):
	project_id = models.CharField(max_length= 120, blank = True, null = True)

class IBM(models.Model):
	api_key = models.CharField(max_length= 120, blank = True, null = True)

class Rackspace(models.Model):
	tenant_id = models.CharField(max_length= 120, blank = True, null = True)