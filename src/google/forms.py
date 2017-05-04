from django import forms
from .models import Google

class GoogleForm(forms.ModelForm):
	class Meta:
		model = Google
		fields = ['project_id', 'client_secret', 'refresh_token']