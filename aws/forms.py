from django import forms
from .models import AWS

def get_zone():
	# user = models.Foreignkey(settings.AUTH_USER_MODEL, blank = False, null = False)
	# print logged_user
	aws_access_key_id = 'AKIAJKLGF55A33R3KTMQ'
	aws_secret_access_key = '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'
	ec2 = boto.connect_ec2(aws_access_key_id=aws_access_key_id,
	aws_secret_access_key=aws_secret_access_key)
	data = ec2.get_all_zones()
	return data

class AWSForm(forms.ModelForm):
	class Meta:
		model = AWS
		fields = ['aws_access_key', 'aws_secret_key', 'account_id']

# class AWSHomeForm(forms.ModelForm):
# 	class Meta:
# 		model = AWSHome
# 		def __init__(self, *args, **kwargs):
# 			data = get_zone()
# 			super(AWSHomeForm, self).__init__(*args, **kwargs)
# 			self.fields['aws_zone'].widget = forms.Select(choices = data)

# class AWSHomeForm(forms.ModelForm):
# 	class Meta:
# 		model = AWS
		

