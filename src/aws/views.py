from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from models import AWS
from .forms import AWSForm, AWSHomeForm
from django.contrib.auth.models import User
import boto
import json
from django.http import HttpResponse

def aws(request):
    aws_object = AWS()
    user_id = request.user.id
    form = AWSForm(request.POST or None)
    print request.POST
    if form.is_valid():
        aws_key = form.cleaned_data['aws_access_key']
        aws_secret = form.cleaned_data['aws_secret_key']
        instance = form.save(commit=False)
        instance.user_id = user_id
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
    test = request.POST.get("zone")
    response_data = {}
    try:
        response_data['result'] = 'done!'
        response_data['message'] = test
    except:
        response_data['result'] = 'nup!'
        response_data['message'] = "not correct"

    # return render_to_response("aws_home.html", context, context_instance = RequestContext(request))
    return HttpResponse(json.dumps(response_data),content_data = "application/json")
    # # if request.method == 'POST':
    # user_id = request.user.id
    # print user_id
    # # aws_model = AWS()
    # # print aws_model.all()
    # aws_access_key_id = ''
    # aws_secret_access_key = ''
    # ec2 = boto.connect_ec2(aws_access_key_id=aws_access_key_id,
    # aws_secret_access_key=aws_secret_access_key)
    # parsed_data = []
    # user_Data = {}
    # # checking all zones
    # # data	= list(ec2.get_all_zones())
    # # list_data = list(boto.ec2.regions())
    # # dict_data = dict(list_data)
    # # print list_data
    # list_data = [1, 2, 3, 4, 5]
    # # data = {key: i for i , key in enumerate(list_data)}
    # form = AWSHomeForm(my_choices = list_data)
    # context = {
    # "form" : form,
    # }
    # return render_to_response("AWS_Home.html", context, context_instance = RequestContext(request))



