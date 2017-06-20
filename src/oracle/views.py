from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from models import ORACLEModel
from .forms import ORACLEForm
from django.http import HttpResponse
from django.contrib.auth.models import User
import json
import boto3
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.db import connection
import base64
from oracle import ORACLE
from datetime import *
from dateutil.tz import *

# Create your views here.

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

def oracle(request):
    print "oracle function"
    usr_id = request.user.id
    # try:
    #     oracle_result = ORACLEModel.objects.get(user_id=usr_id)
    # except:
    #     oracle_result = None
    # if oracle_result is not None:
    #     return render_to_response("oracle_home.html", {}, context_instance=RequestContext(request))
    # else:
    if request.method == 'POST':
        print "oracl function post"
        form = ORACLEForm(request.POST or None)
        if form.is_valid():
            print "form is valid"
            oracle_name = form.cleaned_data['oracle_name']
            encoded_oracle_name = encode(oracle_name)
            oracle_password = form.cleaned_data['oracle_password']
            encoded_oracle_password = encode(oracle_password)
            oracle_domain_name = form.cleaned_data['oracle_domain_name']
            encoded_oracle_domain_name = encode(oracle_domain_name)
            print oracle_name, oracle_password, oracle_domain_name
            keys = ORACLEModel(user_id=usr_id, oracle_name=encoded_oracle_name, 
            	oracle_password=encoded_oracle_password, oracle_domain_name=encoded_oracle_domain_name)
            save_keys = ORACLEModel.save(keys)
            return render_to_response("oracle_home.html", {}, context_instance=RequestContext(request))
    else:
        form = ORACLEForm()

        context = {
            "form": form,
        }
        return render_to_response("oracle_cp.html", context, context_instance=RequestContext(request))


def oracle_cp(request):
    print "oracle cp"
    usr_id = request.user.id
    if request.method == 'POST':
        form = ORACLEForm(request.POST or None)
        if form.is_valid():
            oracle_name = form.cleaned_data['oracle_name']
            encoded_oracle_name = encode(oracle_name)
            print "oracle name ", encoded_oracle_name
            oracle_password = form.cleaned_data['oracle_password']
            encoded_oracle_password = encode(oracle_password)
            print "oracle name ", encoded_oracle_password
            oracle_domain_name = form.cleaned_data['oracle_domain_name']
            encoded_oracle_domain_name= encode(oracle_domain_name)
            print "oracle name ", encoded_oracle_domain_name
            keys = ORACLEModel(user_id=usr_id, oracle_name=encoded_oracle_name, oracle_password=encoded_oracle_password)
            save_keys = ORACLEModel.save(keys)
            print "save done"
            return render_to_response("oracle_home.html", {}, context_instance=RequestContext(request))
    else:
        form = ORACLEForm()

        context = {
            "form": form,
        }
        return render_to_response("oracle_CP.html", context, context_instance=RequestContext(request))


def oracle_create(request):
    if request.method == 'GET':
        return render_to_response("oracle_create.html", {}, context_instance=RequestContext(request))
    else:
        if request.method == 'POST':
            print "I am here"
            shape = str(request.POST.get("shape"))
            image = str(request.POST.get("image_name"))
            print shape, image
            oracle_result = oracle_get_keys(request)
            encoded_oracle_name = str(oracle_result['oracle_name'])
            oracle_name = decode(encoded_oracle_name)
            print "oracle name is ", oracle_name
            encoded_oracle_password = str(oracle_result['oracle_password'])
            oracle_password = decode(encoded_oracle_password)
            print "oracle password is ", oracle_password
            encoded_oracle_domain_name = str(oracle_result['oracle_domain_name'])
            oracle_domain_name = decode(encoded_oracle_domain_name)
            print "oracle domain name is ", oracle_domain_name
            print oracle_name, oracle_password, oracle_domain_name
            oracle = ORACLE(oracle_name, oracle_password, oracle_domain_name)
            print "after init"
            oracle.create_instance(shape, image)
            print "after create instance"
            # oracle.launch_instance("image_id_check", "region_name", min, max, key_name, inst_type, check_status)
            return render_to_response("oracle_home.html", {}, context_instance=RequestContext(request))


def oracle_home(request):
    print "Inside oracle home"
    if request.method == 'POST':
        print "Inside oracle home post"
        selectOP = request.POST.get("selectOP")
    return render_to_response("oracle_home.html", {}, context_instance=RequestContext(request))


def oracle_get_keys(request):
    print " inside get keys "
    usr_id = request.user.id
    oracle_result = ORACLEModel.objects.get(user_id=usr_id)
    print "oracle result ",oracle_result
    oracle_name = str(oracle_result.oracle_name)
    print "oracle_name" , oracle_name
    oracle_password = str(oracle_result.oracle_password)
    print "oracle password", oracle_password
    oracle_domain_name = str(oracle_result.oracle_domain_name)
    print oracle_domain_name
    print oracle_name, oracle_password, oracle_domain_name
    keys = {"oracle_name": oracle_name, "oracle_password": oracle_password, "oracle_domain_name": oracle_domain_name}
    print keys
    return keys

def details_instances(self):
    self.url = 'https://api-z70.compute.us6.oraclecloud.com/instance/Compute-' + self.domain_name + '/' + self.name + '/'
    self.header= {"Cookie": self.mycookie,"Accept": "application/oracle-compute-v3+json"}
    self.request = requests.get(self.url, headers=self.header)
    print self.request.status_code
    print self.request.text

def oracle_delete(request):
    oracle_result = oracle_get_keys(request)
    encoded_oracle_name = str(oracle_result['oracle_name'])
    oracle_name = decode(encoded_oracle_name)
    print "oracle name is ", oracle_name
    encoded_oracle_password = str(oracle_result['oracle_password'])
    oracle_password = decode(encoded_oracle_password)
    print "oracle password is ", oracle_password
    encoded_oracle_domain_name = str(oracle_result['oracle_domain_name'])
    oracle_domain_name = decode(encoded_oracle_domain_name)
    print "oracle domain name is ", oracle_domain_name
    oracle = ORACLE(oracle_name, oracle_password, oracle_domain_name)
    print "after init"
    
    if request.is_ajax():
        if request.method == 'POST':
            instance = str(request.POST.get("instance"))   
            oracle.delete_instance(instance)
            print "after delete instance"
            return render_to_response("oracle_delete.html", {}, context_instance=RequestContext(request))
    return render_to_response("oracle_delete.html", {}, context_instance=RequestContext(request))
