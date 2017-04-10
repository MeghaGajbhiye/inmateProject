from django import forms
from .models import IBM

class IBMForm(forms.ModelForm):
	class Meta:
		model = IBM
		fields = ['api_key']
