from django.db import models
# Create your models here.
class IBM(models.Model):
	# user = models.ForeignKey(AuthUser, unique=True)
	api_key = models.CharField(max_length= 120, blank = True, null = True)
	class Meta:
		managed = False
		db_table = 'ibm'
