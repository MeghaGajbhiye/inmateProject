from django import forms
from models import AWS

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
		

