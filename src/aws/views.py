from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from models import AWS
from .forms import AWSForm, AWSHomeForm
from django.http import HttpResponse
from django.contrib.auth.models import User
import json
import boto
from django.views.generic import TemplateView
from django.http import HttpResponse

def aws(request):
    aws_object = AWS()
    user_id = request.user.id
    form = AWSForm(request.POST or None)
    print request.POST
    if form.is_valid():
        aws_key = form.cleaned_data['aws_access_key']
        aws_secret = form.cleaned_data['aws_secret_key']
        instance = AWS(user_id = user_id, aws_access_key=aws_key, aws_secret_key=aws_secret)
        # instance = form.save(commit=False)
        # instance.user_id = user_id
        # user = User.objects.only('id').get(id = user_id)
        # print user
        # aws_instance = AWS.objects.create(user_id=user)
        # aws_instance.save()
        instance.save()
        print aws_key, aws_secret
    print "form is not valid"
    context = {
        "form": form,
    }
    return render_to_response("AWS_CP.html", context, context_instance = RequestContext(request))



def aws_home(request):
    print "aws_home **************************"
    if request.is_ajax():
        print "it's ajax"
    if request.method == 'POST':
        print "I am here inside post"

        test = request.POST.get("zone")
        print test
        response_data = {}
        try:
            response_data['result'] = 'done!'
            response_data['message'] = test
        except:
            response_data['result'] = 'nup!'
            response_data['message'] = "not correct"

    return render_to_response("aws_home.html", {}, context_instance = RequestContext(request))


def aws_get_keys():
    aws = AWS.objects.raw("Select * from aws where user_id = 4")
    for val in aws:
        access_key = val.aws_access_key
        secret_key = val.aws_secret_key
        print access_key, secret_key
