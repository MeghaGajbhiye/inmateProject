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

region = ""
instance = ""
par = ""
compute_hour = ""


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
    usr_id = request.user.id
    try:
        aws_result = AWSModel.objects.get(user_id=usr_id)
    except:
        aws_result = None
    if aws_result is not None:
        return render_to_response("aws_home.html", {}, context_instance=RequestContext(request))
    else:
        if request.method == 'POST':
            form = AWSForm(request.POST or None)
            if form.is_valid():
                aws_key = form.cleaned_data['aws_access_key']
                encoded_aws_key = encode(aws_key)
                aws_secret = form.cleaned_data['aws_secret_key']
                encoded_aws_secret = encode(aws_secret)
                keys = AWSModel(user_id=usr_id, aws_access_key=encoded_aws_key, aws_secret_key=encoded_aws_secret)
                save_keys = AWSModel.save(keys)
                return render_to_response("aws_home.html", {}, context_instance=RequestContext(request))
        else:
            form = AWSForm()

            context = {
                "form": form,
            }
            return render_to_response("AWS_CP.html", context, context_instance=RequestContext(request))


def aws_cp(request):
    usr_id = request.user.id
    if request.method == 'POST':
        form = AWSForm(request.POST or None)
        if form.is_valid():
            aws_key = form.cleaned_data['aws_access_key']
            encoded_aws_key = encode(aws_key)
            aws_secret = form.cleaned_data['aws_secret_key']
            encoded_aws_secret = encode(aws_secret)
            keys = AWSModel(user_id=usr_id, aws_access_key=encoded_aws_key, aws_secret_key=encoded_aws_secret)
            save_keys = AWSModel.save(keys)
            return render_to_response("aws_home.html", {}, context_instance=RequestContext(request))
    else:
        form = AWSForm()

        context = {
            "form": form,
        }
        return render_to_response("AWS_CP.html", context, context_instance=RequestContext(request))


def aws_create(request):
    if request.method == 'GET':
        return render_to_response("aws_create.html", {}, context_instance=RequestContext(request))
    else:
        if request.method == 'POST':
            inst_name = str(request.POST.get("inst_name"))
            region = str(request.POST.get("region"))
            image = str(request.POST.get("image"))
            inst_type = str(request.POST.get("inst_type"))
            min = int(request.POST.get("min"))
            max = int(request.POST.get("max"))
            key_name = str(request.POST.get("key_name"))
            check_status = eval(request.POST.get("check_status"))
            aws_result = aws_get_keys(request)
            encoded_access_key = str(aws_result['access_key'])
            access_key = decode(encoded_access_key)
            encoded_secret_key = str(aws_result['secret_key'])
            secret_key = decode(encoded_secret_key)
            aws = AWS(access_key, secret_key, 'ec2')
            aws.launch_instance(inst_name, region, image, inst_type, min, max, key_name, check_status)
            aws.launch_instance("image_id_check", "region_name", min, max, key_name, inst_type, check_status)
            return render_to_response("aws_home.html", {}, context_instance=RequestContext(request))


def aws_home(request):
    if request.method == 'POST':
        selectOP = request.POST.get("selectOP")
    return render_to_response("aws_home.html", {}, context_instance=RequestContext(request))
    

def aws_delete(request):
    aws_result = aws_get_keys(request)
    encoded_access_key = str(aws_result['access_key'])
    access_key = decode(encoded_access_key)
    encoded_secret_key = str(aws_result['secret_key'])
    secret_key = decode(encoded_secret_key)
    aws = AWS(access_key, secret_key, 'ec2')
    
    if request.is_ajax():
        if request.method == 'POST':
            region = str(request.POST.get("region"))
            instance = str(request.POST.get("instance"))

            aws_result = aws_get_keys(request)
            encoded_access_key = str(aws_result['access_key'])
            access_key = decode(encoded_access_key)
            encoded_secret_key = str(aws_result['secret_key'])
            secret_key = decode(encoded_secret_key)
            aws = AWS(access_key, secret_key, 'ec2')
            aws.terminate_instance(instance, region)

            return render_to_response("aws_delete.html", {}, context_instance=RequestContext(request))
    return render_to_response("aws_delete.html", {}, context_instance=RequestContext(request))

def aws_view(request):
    global region
    if request.method == 'POST':
        region = str(request.POST.get("region"))
        aws_result = aws_get_keys(request)
        encoded_access_key = str(aws_result['access_key'])
        access_key = decode(encoded_access_key)
        encoded_secret_key = str(aws_result['secret_key'])
        secret_key = decode(encoded_secret_key)
        aws = AWS(access_key, secret_key, 'ec2')

        return render_to_response("aws_view_list.html", {}, context_instance=RequestContext(request))
    return render_to_response("aws_view.html", {},
                                  context_instance=RequestContext(request))


def aws_view_list(request):
    global region
    if request.is_ajax():
        if request.method == 'POST':
            aws_result = aws_get_keys(request)
            encoded_access_key = str(aws_result['access_key'])
            access_key = decode(encoded_access_key)
            encoded_secret_key = str(aws_result['secret_key'])
            secret_key = decode(encoded_secret_key)

            aws = AWS(access_key, secret_key, 'ec2')
            instance_list = aws.describe_instances(region)
            return render_to_response("aws_home.html", {}, context_instance=RequestContext(request))
    else:
        aws_result = aws_get_keys(request)
        encoded_access_key = str(aws_result['access_key'])
        access_key = decode(encoded_access_key)
        encoded_secret_key = str(aws_result['secret_key'])
        secret_key = decode(encoded_secret_key)
        aws = AWS(access_key, secret_key, 'ec2')
        aws.describe_instances(region)
        instance_list = aws.describe_instances(region)
        instance_db = instance_list
        return render_to_response("aws_view_list.html", {'instance_db': instance_db}, context_instance=RequestContext(request))


def aws_get_keys(request):
    usr_id = request.user.id
    aws_result = AWSModel.objects.get(user_id=usr_id)
    access_key = str(aws_result.aws_access_key)
    secret_key = str(aws_result.aws_secret_key)
    keys = {"access_key": access_key, "secret_key": secret_key}
    return keys

def aws_monitor_list(request):
    global region, instance, par, compute_hour
    if request.is_ajax():
        if request.method == 'POST':
            region = str(request.POST.get("region"))
            instance = str(request.POST.get("instance"))
            par = str(request.POST.get("par"))
            compute_hour = int(request.POST.get("hours"))
            aws_result = aws_get_keys(request)
            encoded_access_key = str(aws_result['access_key'])
            access_key = decode(encoded_access_key)
            encoded_secret_key = str(aws_result['secret_key'])
            secret_key = decode(encoded_secret_key)
            aws = AWS(access_key, secret_key, 'ec2')
            aws_monitor(request)
    return render_to_response("aws_monitor_list.html", {"par": par}, context_instance=RequestContext(request))

def aws_monitor(request):

    global instance, region, par, compute_hour
    aws_result = aws_get_keys(request)
    encoded_access_key = str(aws_result['access_key'])
    access_key = decode(encoded_access_key)
    encoded_secret_key = str(aws_result['secret_key'])
    secret_key = decode(encoded_secret_key)
    aws = AWS(access_key, secret_key, 'cloudwatch')
    data1 = aws.get_metrics(instance, region, compute_hour, par)
    return render_to_response("aws_monitor.html",{"data1": data1}, context_instance=RequestContext(request))

