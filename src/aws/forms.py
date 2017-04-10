from django import forms
from models import AWS


class AWSForm(forms.ModelForm):
    class Meta:
        model = AWS
        fields = ['aws_access_key', 'aws_secret_key', 'account_id']

        def clean_aws_key(self):
            aws_key = self.cleaned_data.get("aws_access_key")
            if aws_key == " " or aws_key is None:
                raise forms.ValidationError("Please enter aws keys")
            return aws_key

        def clean_secret_key(self):
            secret_key = self.cleaned_data.get("aws_secret_key")
            if secret_key == " " or secret_key is None:
               raise forms.ValidationError("Please enter aws keys")
            return secret_key





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
