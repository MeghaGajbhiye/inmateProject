from django import forms
from .models import Rackspace

class RackspaceForm(forms.ModelForm):
	class Meta:
		model = Rackspace
		fields = ['tenant_id']
	
	def __init__(self, *args, **kwargs):
		super(RackspaceForm, self).__init__(*args, **kwargs)
		for field in self.fields:
			help_text = self.fields[field].help_text
			self.fields[field].help_text = None
			if help_text != '':
				self.fields[field].widget.attrs.update({'class':'has-popover', 'data-content':help_text, 'data-placement':'right', 'data-container':'body'})
