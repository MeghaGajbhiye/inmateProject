from django import forms
from .models import Azure

class AzureForm(forms.ModelForm):
	class Meta:
		model = Azure
		fields = ['enrollment_number', 'api_key']
