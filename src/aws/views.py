from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from models import AWSModel
from .forms import AWSForm, AWSHomeForm
from django.http import HttpResponse
from django.contrib.auth.models import User
import json
import boto3
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.db import connection
import base64
from aws import AWS
from datetime import *
from dateutil.tz import *

def encode(value):
    key = "autum"
    enc = []
    for i in range(len(value)):
        key_c = key[i % len(key)]
        enc_c = chr((ord(value[i]) + ord(key_c)) % 256)
        enc.append(enc_c)
    encoded_val = base64.urlsafe_b64encode("".join(enc))
    return encoded_val

def decode(enc):
    key = "autum"
    dec = []
    enc = base64.urlsafe_b64decode(enc)
    for i in range(len(enc)):
        key_c = key[i % len(key)]
        dec_c = chr((256 + ord(enc[i]) - ord(key_c)) % 256)
        dec.append(dec_c)
    return "".join(dec)

def aws(request):
    print "In aws function 123"
    usr_id = request.user.id
    print usr_id
    # Get the user Id of logged in user
    try:
        aws_result = AWSModel.objects.get(user_id=usr_id)
        print "aws reult is", aws_result
    except:
        aws_result = None
    if aws_result is not None:
        print "not none"
        return render_to_response("aws_home.html", {}, context_instance=RequestContext(request))
    else:
        if request.method == 'POST':
            print "it is post"
            form = AWSForm(request.POST or None)
            if form.is_valid():
                aws_key = form.cleaned_data['aws_access_key']
                encoded_aws_key = encode(aws_key)
                aws_secret = form.cleaned_data['aws_secret_key']
                encoded_aws_secret = encode(aws_secret)
                print encoded_aws_key, encoded_aws_secret
                keys = AWSModel(user_id=usr_id, aws_access_key=encoded_aws_key, aws_secret_key=encoded_aws_secret)
                save_keys = AWSModel.save(keys)
                print "AWS KEYS HAS BEEN SAVED IN AWS TABLE"
                return render_to_response("aws_home.html", {}, context_instance=RequestContext(request))
        else:
            form = AWSForm()

            context = {
                "form": form,
            }
            print "I am printing aws cp"
            return render_to_response("AWS_CP.html", context, context_instance=RequestContext(request))


def aws_cp(request):
    usr_id = request.user.id
    if request.method == 'POST':
        print "it is post"
        form = AWSForm(request.POST or None)
        if form.is_valid():
            aws_key = form.cleaned_data['aws_access_key']
            encoded_aws_key = encode(aws_key)
            aws_secret = form.cleaned_data['aws_secret_key']
            encoded_aws_secret = encode(aws_secret)
            print encoded_aws_key, encoded_aws_secret
            keys = AWSModel(user_id=usr_id, aws_access_key=encoded_aws_key, aws_secret_key=encoded_aws_secret)
            save_keys = AWSModel.save(keys)
            print "AWS KEYS HAS BEEN SAVED IN AWS TABLE"
            return render_to_response("aws_home.html", {}, context_instance=RequestContext(request))
    # Else if the request method is GET that means user is visiting the AWS Signup form, therefore AWS
    # sign up form is shown to the user
    else:
        form = AWSForm()

        context = {
            "form": form,
        }
        print "I am printing aws cp"
        return render_to_response("AWS_CP.html", context, context_instance=RequestContext(request))


def aws_create(request):
    print "aws create ********"
    # If the request method is Get, show the create form to the user
    if request.is_ajax():
        print "it's ajax"

    if request.method == 'GET':
        print "inside get"
        return render_to_response("aws_create.html", {}, context_instance=RequestContext(request))

    # else if the request methos is POST that means user has filled the form and posting the data in order to
    # create an instance, therefore fetching the POST values from the aws_create.html and calling the create_instance
    # function in order to create a new instance
    else:
        if request.is_ajax():
            print "it's ajax"
        if request.method == 'POST':
            print "Inside post"
            inst_name = str(request.POST.get("inst_name"))
            region = str(request.POST.get("region"))
            image = str(request.POST.get("image"))
            inst_type = str(request.POST.get("inst_type"))
            min = int(request.POST.get("min"))
            max = int(request.POST.get("max"))
            key_name = str(request.POST.get("key_name"))
            check_status = eval(request.POST.get("check_status"))

            print inst_name, region, image, inst_type, min, max, key_name, check_status

            aws_result = aws_get_keys(request)
            encoded_access_key = str(aws_result['access_key'])
            access_key = decode(encoded_access_key)
            encoded_secret_key = str(aws_result['secret_key'])
            secret_key = decode(encoded_secret_key)
            print encoded_access_key, access_key, encoded_secret_key, secret_key
            print "I am here after encoding"

            aws = AWS(access_key, secret_key)


            aws.launch_instance(inst_name, region, image, inst_type, min, max, key_name, check_status)

            print "here after aws setting keys"
            aws.launch_instance("image_id_check", "region_name", min, max, key_name, inst_type, check_status)


            # return HttpResponse(json.dumps({'message': "Success"}), content_type="application/json")

            return render_to_response("aws_home.html", {}, context_instance=RequestContext(request))


def aws_home(request):
    print "aws_inst **************************"

    # if request.method == 'POST':
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
    # # data   = list(ec2.get_all_zones())
    # list_data = list(boto.ec2.regions())
    # # dict_data = dict(list_data)
    # # print list_data
    # list_data = [(1, 'region1'), (2, 'region2'), (3,'region3')]
    # # data = {key: i for i , key in enumerate(list_data)}
    # form = AWSHomeForm(my_choices = list_data)
    # context = {
    # "form" : form,
    # }
    # aws_get_keys()
    # test = request.POST.get("zone", "region", "image", "min_count", "max_count", "key_name", "inst_type", "monitoring")
    if request.is_ajax():
        print "it's ajax"
    if request.method == 'POST':
        print "I am here inside post"

        selectOP = request.POST.get("selectOP")

        print selectOP

    return render_to_response("aws_home.html", {}, context_instance=RequestContext(request))
    # return HttpResponse(json.dumps(response_data),content_type="application/json")


def aws_delete(request):
    print "aws_delete **************************"
    aws_result = aws_get_keys(request)
    encoded_access_key = str(aws_result['access_key'])
    access_key = decode(encoded_access_key)
    encoded_secret_key = str(aws_result['secret_key'])
    secret_key = decode(encoded_secret_key)
    aws = AWS(access_key, secret_key)
    print "I am above instance list"


    if request.is_ajax():
        print "it's ajax"
        if request.method == 'POST':
            print 'in delete post1234'

            # print "I am here inside post"
            region = str(request.POST.get("region"))
            instance = str(request.POST.get("instance"))

            print region, instance
            # Get AWS Access key and secret key from database
            # Instantiate AWS class aws->aws.py and calling the launch_instance function
            aws_result = aws_get_keys(request)
            encoded_access_key = str(aws_result['access_key'])
            access_key = decode(encoded_access_key)
            encoded_secret_key = str(aws_result['secret_key'])
            secret_key = decode(encoded_secret_key)
            print encoded_access_key, access_key, encoded_secret_key, secret_key
            print "I am here after encoding"
            aws = AWS(access_key, secret_key)
            aws.terminate_instance(instance, region)

            return render_to_response("aws_delete.html", {}, context_instance=RequestContext(request))
    print "in get method"
    return render_to_response("aws_delete.html", {}, context_instance=RequestContext(request))

# def aws_view_delete(request):
#     print "aws_view_delete **************************"
#     if request.is_ajax():
#         print "it's ajax"
#         if request.method == 'POST':
#             print 'in delete post-view-del'
#             region = request.POST.get("region")
#             print region
#             # Get AWS Access key and secret key from database
#             # Instantiate AWS class aws->aws.py and calling the launch_instance function
#             # aws_result = aws_get_keys(request)
#             # encoded_access_key = str(aws_result['access_key'])
#             # access_key = decode(encoded_access_key)
#             # encoded_secret_key = str(aws_result['secret_key'])
#             # secret_key = decode(encoded_secret_key)
#             # print encoded_access_key, access_key, encoded_secret_key, secret_key
#             print "I am here after encoding"
#             #instance_db = [your data from db]
#             print 'in asw vie del'
#             # return render_to_response("aws_delete.html",{})
#             return render_to_response("aws_view.html", {})
#     else:
#         print 'google'
#         return render_to_response("aws_view_delete.html",{})
def aws_view(request):
    print "aws_view **************************"
    if request.is_ajax():
        print "it's ajax"
    if request.method == 'POST':

        print "I am here inside post"
        region = str(request.POST.get("region"))

        print region
        aws_result = aws_get_keys(request)
        encoded_access_key = str(aws_result['access_key'])
        access_key = decode(encoded_access_key)
        encoded_secret_key = str(aws_result['secret_key'])
        secret_key = decode(encoded_secret_key)
        print encoded_access_key, access_key, encoded_secret_key, secret_key
        print "I am here after encoding"
        aws = AWS(access_key, secret_key)
        print "I am above instance_list"
        instance_list = json.dumps(aws.describe_instances(region))
        print "printing instance list"
        print instance_list
        return render_to_response("aws_home.html", {}, context_instance=RequestContext(request))
    else:
        print "in get"

        aws_result = aws_get_keys(request)
        encoded_access_key = str(aws_result['access_key'])
        access_key = decode(encoded_access_key)
        encoded_secret_key = str(aws_result['secret_key'])
        secret_key = decode(encoded_secret_key)
        print encoded_access_key, access_key, encoded_secret_key, secret_key
        print "I am here after encoding"
        aws = AWS(access_key, secret_key)
        instance_list = json.dumps(aws.describe_instances(list))
        print "printing instance list in get"
        print instance_list[0]
        instance_db = instance_list
        return render_to_response("aws_view.html", {},
                                  context_instance=RequestContext(request))







# def aws_view(request):
#     print "aws_view_list **************************"
#
#     if request.is_ajax():
#         print "it's ajax"
#         if request.method == 'POST':
#             print "I am here inside post"
#             region = request.POST.get("region")
#
#
#             # Get AWS Access key and secret key from database
#             # Instantiate AWS class aws->aws.py and calling the launch_instance function
#             aws_result = aws_get_keys(request)
#             encoded_access_key = str(aws_result['access_key'])
#             access_key = decode(encoded_access_key)
#             encoded_secret_key = str(aws_result['secret_key'])
#             secret_key = decode(encoded_secret_key)
#             print encoded_access_key, access_key, encoded_secret_key, secret_key
#             print "I am here after encoding"
#
#             aws = AWS(access_key, secret_key)
#             aws.describe_instances(region)
#             print "I am above instance list"
#             # instance_list = json.dumps(aws.describe_instances(region))
#             # print "printing instance list"
#             # print instance_list
#         return render_to_response("aws_view.html", {}, context_instance=RequestContext(request))
        # else:
        #     print "in get"
        #     region = request.POST.get("region")
        #     aws_result = aws_get_keys(request)
        #     encoded_access_key = str(aws_result['access_key'])
        #     access_key = decode(encoded_access_key)
        #     encoded_secret_key = str(aws_result['secret_key'])
        #     secret_key = decode(encoded_secret_key)
        #     aws = AWS(access_key, secret_key)
        #     aws.describe_instances(region)
        #     print "I am above instance list"
        #     instance_list = json.dumps(aws.describe_instances(region))
        #     print "printing instance list in get"
        #     print instance_list[0]
        #     instance_db = instance_list
        #     return render_to_response("aws_view.html", {'instance_db': instance_db}, context_instance=RequestContext(request))




def aws_get_keys(request):
    # print "I am inside aws_get_keys"
    # aws = AWS.objects.raw("Select * from aws where user_id = 4")
    # for val in aws:
    #     access_key = val.aws_access_key
    #     secret_key = val.aws_secret_key
    #     print access_key, secret_key
    print "get keys"
    usr_id = request.user.id
    aws_result = AWSModel.objects.get(user_id=usr_id)
    access_key = str(aws_result.aws_access_key)
    secret_key = str(aws_result.aws_secret_key)
    print access_key, secret_key
    keys = {"access_key": access_key, "secret_key": secret_key}
    return keys

def aws_monitor_list(request):
    print "aws_monitor_list **************************"

    if request.is_ajax():
        print "it's ajax"
        if request.method == 'POST':
            print "I am here inside post"
            region = str(request.POST.get("region"))
            instance = str(request.POST.get("instance"))

            print region, instance
            # Get AWS Access key and secret key from database
            # Instantiate AWS class aws->aws.py and calling the launch_instance function
            aws_result = aws_get_keys(request)
            encoded_access_key = str(aws_result['access_key'])
            access_key = decode(encoded_access_key)
            encoded_secret_key = str(aws_result['secret_key'])
            secret_key = decode(encoded_secret_key)
            print encoded_access_key, access_key, encoded_secret_key, secret_key
            print "I am here after encoding"
            aws = AWS(access_key, secret_key)
            # aws.describe_instances(region, instance)
            # instance_list = aws.describe_instances(region, instance)
            print "printing instance list in get"
            aws_monitor(request)
            # return render_to_response("aws_monitor.html", {}, context_instance=RequestContext(request))
    return render_to_response("aws_monitor_list.html", {}, context_instance=RequestContext(request))

def aws_monitor(request):

    instance_id = "abc"
    aws_result = aws_get_keys(request)
    encoded_access_key = str(aws_result['access_key'])
    access_key = decode(encoded_access_key)
    encoded_secret_key = str(aws_result['secret_key'])
    secret_key = decode(encoded_secret_key)
    print encoded_access_key, access_key, encoded_secret_key, secret_key
    print "I am here after encoding"

    aws = AWS(access_key, secret_key)
    data1 = aws.get_metrics("i-0cae18706985f552e", "us-west-2")
    print "data1:::::::::::::::::::::::::::::::::::::", data1
    # data1 = [['datetime.datetime(2017, 5, 10, 23, 30, tzinfo=tzutc())', 0.0], ['datetime.datetime(2017, 5, 11, 0, 30, tzinfo=tzutc())', 0.0]]
    print data1
    return render_to_response("aws_monitor.html",{"data1": data1}, context_instance=RequestContext(request))

