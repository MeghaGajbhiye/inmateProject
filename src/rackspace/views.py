from django.shortcuts import render
from django.template import RequestContext
from django.shortcuts import render_to_response
from .forms import RackspaceForm
from models import Rackspace
from django.http import HttpResponse
from django.contrib.auth.models import User
import json
import boto3
from django.views.generic import TemplateView
from django.http import HttpResponse
import base64
from rackspace import Rackspace as r



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


# Create your views here.
def rackspace(request):
    usr_id = request.user.id
    try:
        rackspace_result = Rackspace.objects.get(id=usr_id)
    except:
        rackspace_result = None
    if rackspace_result is not None:
        return render_to_response("rackspace_home.html", {}, context_instance=RequestContext(request))
    else:
        if request.method == 'POST':
            print "it is post"
            form = RackspaceForm(request.POST or None)
            if form.is_valid():
                username = form.cleaned_data['username']
                api_key = form.cleaned_data['api_key']
                encoded_api_key = encode(api_key)
                keys = Rackspace(id=usr_id, username=username, api_key=encoded_api_key)
                save_keys = Rackspace.save(keys)
                print "Rackspace KEYS HAS BEEN SAVED IN Rackspace TABLE"
                return render_to_response("rackspace_home.html", {}, context_instance=RequestContext(request))
        else:
            form = RackspaceForm()
            context = {
                "form": form,
            }
            return render_to_response("Rackspace.html", context, context_instance=RequestContext(request))


def rackspace_create(request):
    print "rackspace_create **************************"
    # if request.is_ajax():
    #     print "it's ajax"
    if request.method == 'GET':
        return render_to_response("rackspace_create.html", {}, context_instance=RequestContext(request))
    if request.method == 'POST':
        print "I am here inside post"
        instance = str(request.POST.get("instance"))
        selectram = int(request.POST.get("selectram"))
        selectimage = str(request.POST.get("selectimage"))
        rackspace_result = rackspace_get_keys(request)
        username = str(rackspace_result['username'])
        encoded_api_key = str(rackspace_result['api_key'])
        print username, encoded_api_key
        api_key = decode(encoded_api_key)
        print "I am here after encoding"
        print (username, api_key)
        print username, api_key
        rackspace = r(username, api_key)
        rackspace.launch_instance(instance, selectimage, selectram)
        # return render_to_response("rackspace_home.html", {}, context_instance=RequestContext(request))
    return render_to_response("rackspace_create.html", {}, context_instance=RequestContext(request))
        # elif request.method == 'GET':
        #     return render_to_response("rackspace_create.html", {})


def rackspace_home(request):
    print "rackspace_home **************************"
    if request.is_ajax():
        print "it's ajax"
    if request.method == 'POST':
        print "I am here inside post"
        selectOP = request.POST.get("selectOP")
        print selectOP
    return render_to_response("rackspace_home.html", {}, context_instance=RequestContext(request))



def rackspace_update(request):
    print "rackspace_update **************************"
    if request.is_ajax():
        print "it's ajax"
    if request.method == 'POST':

        print "I am here inside post"
        instance = str(request.POST.get("instance"))
        selectram = int(request.POST.get("selectram"))
        rackspace_result = rackspace_get_keys(request)
        username = str(rackspace_result['username'])
        encoded_api_key = str(rackspace_result['api_key'])
        print username, encoded_api_key
        api_key = decode(encoded_api_key)
        # print "I am here after encoding"
        print (username, api_key)
        rackspace = r(username, api_key)

        rackspace.update_instance(instance, selectram)
        print "I am above instance_list"
        instance_list = json.dumps(rackspace.view_instances())
        print "printing instance list"
        print instance_list
        return render_to_response("rackspace_home.html", {}, context_instance=RequestContext(request))
    else:
        print "in get"
        rackspace_result = rackspace_get_keys(request)
        username = str(rackspace_result['username'])
        encoded_api_key = str(rackspace_result['api_key'])
        api_key = decode(encoded_api_key)
        rackspace = r(username, api_key)
        instance_list = rackspace.view_instances()
        print "printing instance list in get"
        print instance_list[0]
        instance_db = instance_list
        return render_to_response("rackspace_update.html", {'instance_db': instance_db}, context_instance=RequestContext(request))
   
        
def rackspace_delete(request):
    print "rackspace_delete **************************"
    if request.is_ajax():
        print "it's ajax"
    if request.method == 'POST':

        print "I am here inside post"
        instance = request.POST.get("instance")

        rackspace_result = rackspace_get_keys(request)
        username = str(rackspace_result['username'])
        encoded_api_key = str(rackspace_result['api_key'])
        print username, encoded_api_key
        api_key = decode(encoded_api_key)
        # print "I am here after encoding"
        print (username, api_key)
        rackspace = r(username, api_key)

        rackspace.delete_instance(instance)
        print "I am above instance_list"
        instance_list = json.dumps(rackspace.view_instances())
        print "printing instance list"
        print instance_list
        return render_to_response("rackspace_home.html", {}, context_instance=RequestContext(request))
    else:
        print "in get"
        rackspace_result = rackspace_get_keys(request)
        username = rackspace_result['username']
        encoded_api_key = rackspace_result['api_key']
        api_key = decode(encoded_api_key)
        rackspace = r(username, api_key)
        instance_list = rackspace.view_instances()
        print "printing instance list in get"
        print instance_list[0]
        instance_db = instance_list
        return render_to_response("rackspace_delete.html", {'instance_db': instance_db},
                                  context_instance=RequestContext(request))



def rackspace_reboot(request):
    print "rackspace_reboot **************************"
    if request.is_ajax():
        print "it's ajax"
    if request.method == 'POST':

        print "I am here inside post"
        instance = str(request.POST.get("instance"))
        boot = str(request.POST.get("boot"))
        rackspace_result = rackspace_get_keys(request)
        username = str(rackspace_result['username'])
        encoded_api_key = str(rackspace_result['api_key'])
        print username, encoded_api_key
        api_key = decode(encoded_api_key)
        # print "I am here after encoding"
        print (username, api_key)
        rackspace = r(username, api_key)

        rackspace.instance_reboot(instance, boot)
        print "I am above instance_list"
        instance_list = json.dumps(rackspace.view_instances())
        print "printing instance list"
        print instance_list
        return render_to_response("rackspace_home.html", {}, context_instance=RequestContext(request))
    else:
        print "in get"
        rackspace_result = rackspace_get_keys(request)
        username = str(rackspace_result['username'])
        encoded_api_key = str(rackspace_result['api_key'])
        api_key = decode(encoded_api_key)
        rackspace = r(username, api_key)
        instance_list = rackspace.view_instances()
        print "printing instance list in get"
        print instance_list[0]
        instance_db = instance_list
        return render_to_response("rackspace_reboot.html", {'instance_db': instance_db},
                                  context_instance=RequestContext(request))


def rackspace_view(request):
    print "rackspace_view **************************"
    if request.is_ajax():
        print "it's ajax"
    if request.method == 'POST':

        print "I am here inside post"

        rackspace_result = rackspace_get_keys(request)
        username = str(rackspace_result['username'])
        encoded_api_key = str(rackspace_result['api_key'])
        print username, encoded_api_key
        api_key = decode(encoded_api_key)
        # print "I am here after encoding"
        print (username, api_key)
        rackspace = r(username, api_key)

        rackspace.view_instances()
        print "I am above instance_list"
        instance_list = json.dumps(rackspace.view_instances())
        print "printing instance list"
        print instance_list
        return render_to_response("rackspace_home.html", {}, context_instance=RequestContext(request))
    else:
        print "in get"
        rackspace_result = rackspace_get_keys(request)
        username = str(rackspace_result['username'])
        encoded_api_key = str(rackspace_result['api_key'])
        api_key = decode(encoded_api_key)
        rackspace = r(username, api_key)
        instance_list = rackspace.view_instances()
        print "printing instance list in get"
        print instance_list[0]
        instance_db = instance_list
        return render_to_response("rackspace_view.html", {'instance_db': instance_db},
                                  context_instance=RequestContext(request))


def rackspace_get_keys(request):
    usr_id = request.user.id
    rackspace_result = Rackspace.objects.get(id=usr_id)
    username = str(rackspace_result.username)
    api_key = str(rackspace_result.api_key)
    print username, api_key, "inside get keys"
    keys = {"username": username, "api_key": api_key}
    return keys

def rackspace_monitor(request):
    print "****************************************rackspace_monitor **************************"

    rackspace_result = rackspace_get_keys(request)
    username = rackspace_result['username']
    encoded_api_key = str(rackspace_result['api_key'])
    print username, encoded_api_key
    api_key = decode(encoded_api_key)
    # print "I am here after encoding"
    print (username, api_key)
    rackspace = r(username, api_key)
    instance_list = json.dumps(rackspace.view_instances())  # list of instances - pushpa
    print instance_list

    if request.is_ajax():
        print "it's ajax"
        if request.method == 'POST':
            print "I am here inside post"
            instance_name = request.POST.get("instance_name")
            alarm = str(request.POST.get("alarm"))
            email = str(request.POST.get("email"))
            print instance_name, alarm, email
            instance_list = json.dumps(rackspace.view_instances()) # list of instances - pushpa
            print instance_list
            context = {"instance_list": instance_list}
            print instance_list
            
            alarm_db = [u'CPU', u'Memory', u'Ping', u'5-Minute Load Average']
            print "I am above alarm"
            alarm_name = json.dumps(alarm_db)
            print alarm_name
            context = {"alarm_name": alarm_name}
            print "Gotcha instance"
            return render_to_response("rackspace_monitor.html", {}, context_instance=RequestContext(request))
    elif request.method == 'GET':
        instance_db = instance_list
        alarm_db = [u'CPU', u'Memory', u'Ping', u'5-Minute Load Average']
        return render_to_response("rackspace_monitor.html", {'alarm_db': alarm_db, 'instance_db': instance_list})

