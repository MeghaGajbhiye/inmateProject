from django import forms
from .models import Rackspace

class RackspaceForm(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(RackspaceForm, self).__init__(*args, **kwargs)
		self.fields['username'].help_text = '<br/>Enter username of Rackspace'

	class Meta:
		model = Rackspace
		fields = ['username', 'api_key']


