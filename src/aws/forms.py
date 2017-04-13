from django import forms
from models import AWS
import boto


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
#     class Meta:
#         model = AWSHome
#         fields = ['aws_zone']

def get_zone():
    aws_access_key_id = 'AKIAJKLGF55A33R3KTMQ'
    aws_secret_access_key = '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'
    ec2 = boto.connect_ec2(aws_access_key_id=aws_access_key_id,
                           aws_secret_access_key=aws_secret_access_key)
    # data = list(ec2.get_all_zones())
    data = list(boto.ec2.regions())
    return data


class AWSHomeForm(forms.Form):
    def __init__(self,*args, **kwargs):
        choices = kwargs.pop('my_choices')
        super(AWSHomeForm, self).__init__(*args, **kwargs)
        self.fields["aws_zone"] = forms.ChoiceField(choices=choices)
