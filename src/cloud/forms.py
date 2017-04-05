from django import forms
from .models import SignUp, AWS, Azure, Google, Rackspace, IBM

class ContactForm(forms.Form):
	full_name = forms.CharField()
	email= forms.EmailField()
	message = forms.CharField()

	def clean_email(self):
		email =  self.cleaned_data.get("email")
		email_base, provider = email.split("@")
		domain, extension =  provider.split('.')
		if not domain == "sjsu":
			raise forms.ValidationError("Please use a valid SJSU email address")
		if not extension == "edu":
		# if not "edu" in email:
			raise forms.ValidationError("Please use a valid .EDU email address")
		return email



class SignUpForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput)
	class Meta:
		model = SignUp
		fields = ['full_name','email', 'password']

	def clean_email(self):
		email =  self.cleaned_data.get("email")
		email_base, provider = email.split("@")
		domain, extension =  provider.split('.')
		if not domain == "sjsu":
			raise forms.ValidationError("Please use a valid SJSU email address")
		if not extension == "edu":
		# if not "edu" in email:
			raise forms.ValidationError("Please use a valid .EDU email address")
		return email

	# def clean_full_name(self):
	# 	full_name = self.cleaned_data.get('full_name')


class AWSForm(forms.ModelForm):
	class Meta:
		model = AWS
		fields = ['aws_access_key', 'aws_secret_key', 'account_id']

class AzureForm(forms.ModelForm):
	class Meta:
		model = Azure
		fields = ['enrollment_number', 'api_key']

class GoogleForm(forms.ModelForm):
	class Meta:
		model = Google
		fields = ['project_id']

class IBMForm(forms.ModelForm):
	class Meta:
		model = IBM
		fields = ['api_key']

class RackspaceForm(forms.ModelForm):
	class Meta:
		model = Rackspace
		fields = ['tenant_id']