from django import forms
from .models import Rackspace

class RackspaceForm(forms.ModelForm):
	class Meta:
		model = Rackspace
		fields = ['tenant_id']