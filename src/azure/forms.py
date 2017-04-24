from django import forms
from .models import Azure

class AzureForm(forms.ModelForm):
	class Meta:
		model = Azure
		fields = ['subscription_id', 'client_id', 'secret_key', 'tenant_id']
