from django import forms
from .models import ORACLEModel

class ORACLEForm(forms.ModelForm):
	oracle_password = forms.CharField(widget=forms.PasswordInput)
	class Meta:
		model = ORACLEModel
		fields = ['oracle_name', 'oracle_password', 'oracle_domain_name']
