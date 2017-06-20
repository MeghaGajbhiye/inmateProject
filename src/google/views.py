from django.shortcuts import render
from django.template import RequestContext
from django.shortcuts import render_to_response
from models import Google
from .forms import GoogleForm
from django.http import HttpResponse
from django.contrib.auth.models import User
import json
import boto3
from django.views.generic import TemplateView
from django.http import HttpResponse
from google import Google as G
import base64
pro_id = ""
zone = ""


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

def google(request):
    usr_id = request.user.id
    try:
        google_result = Google.objects.get(id=usr_id)
    except:
        google_result = None
    if google_result is not None:
        return render_to_response("google_home.html", {}, context_instance=RequestContext(request))
    else:
        if request.method == 'POST':
           form = GoogleForm(request.POST or None)
           if form.is_valid():
               project_id = form.cleaned_data['project_id']
               encoded_project_id = encode(project_id)
               client_secret = form.cleaned_data['client_secret']
               encoded_client_secret = encode(client_secret)
               refresh_token = form.cleaned_data['refresh_token']
               encoded_refresh_token = encode(refresh_token)
               keys = Google(id=usr_id, project_id=encoded_project_id, client_secret=encoded_client_secret, refresh_token=encoded_refresh_token)
               save_keys = Google.save(keys)
               return render_to_response("google_home.html", {}, context_instance=RequestContext(request))
        else:
            form = GoogleForm()
            context = {
                "form": form,
            }
            return render_to_response("Google_CP.html", context, context_instance=RequestContext(request))


def google_cp(request):
    usr_id = request.user.id
    if request.method == 'POST':
        form = GoogleForm(request.POST or None)
        if form.is_valid():
            project_id = form.cleaned_data['project_id']
            encoded_project_id = encode(project_id)
            client_secret = form.cleaned_data['client_secret']
            encoded_client_secret = encode(client_secret)
            refresh_token = form.cleaned_data['refresh_token']
            encoded_refresh_token = encode(refresh_token)
            keys = Google(id=usr_id, project_id=encoded_project_id, client_secret=encoded_client_secret,
                          refresh_token=encoded_refresh_token)
            save_keys = Google.save(keys)
            return render_to_response("google_home.html", {}, context_instance=RequestContext(request))
    else:
        form = GoogleForm()
        context = {
            "form": form,
        }
        return render_to_response("Google_CP.html", context, context_instance=RequestContext(request))



def google_home(request):
    if request.method == 'POST':
        selectOP = request.POST.get("selectOP")
    return render_to_response("google_home.html", {}, context_instance=RequestContext(request))


def google_create(request):
    if request.method == 'POST':
        selectzone = str(request.POST.get("selectzone"))
        Pro_id = str(request.POST.get("Pro_id"))
        Buck_id = str(request.POST.get("Buck_id"))
        Inst_name = str(request.POST.get("Inst_name"))
        usr_id = request.user.id
        google_result = google_get_keys(request)
        encoded_project_id = str(google_result["project_id"])
        project_id = decode(encoded_project_id)
        encoded_client_secret = str(google_result["client_secret"])
        client_secret = decode(encoded_client_secret)
        encoded_refresh_token = str(google_result["refresh_token"])
        refresh_token = decode(encoded_refresh_token)
        google = G(project_id, client_secret, refresh_token)
        google.create_instance(Pro_id, selectzone,  Inst_name, Buck_id)
        return render_to_response("google_home.html", {}, context_instance=RequestContext(request))
    elif request.method == 'GET':
        return render_to_response("google_create.html", {}, context_instance=RequestContext(request))

def google_retrieve(request):
    global pro_id, zone
    if request.method == 'POST':
        zone = str(request.POST.get("selectzone"))
        pro_id = str(request.POST.get("pro_id"))
        google_result = google_get_keys(request)
        encoded_project_id = str(google_result["project_id"])
        project_id = decode(encoded_project_id)
        encoded_client_secret = str(google_result["client_secret"])
        client_secret = decode(encoded_client_secret)
        encoded_refresh_token = str(google_result["refresh_token"])
        refresh_token = decode(encoded_refresh_token)
        return render_to_response("google_view.html", {}, context_instance=RequestContext(request))
    return render_to_response("google_retrieve.html", {}, context_instance=RequestContext(request))

def google_view(request):
    global pro_id, zone
    if request.method == 'POST':
        google_result = google_get_keys(request)
        encoded_project_id = str(google_result["project_id"])
        project_id = decode(encoded_project_id)
        encoded_client_secret = str(google_result["client_secret"])
        client_secret = decode(encoded_client_secret)
        encoded_refresh_token = str(google_result["refresh_token"])
        refresh_token = decode(encoded_refresh_token)
        google = G(project_id, client_secret, refresh_token)
        instance_list = json.dumps(google.list_instances(pro_id, zone))
        return render_to_response("google_home.html", {}, context_instance=RequestContext(request))
    else:
        google_result = google_get_keys(request)
        encoded_project_id = str(google_result["project_id"])
        project_id = decode(encoded_project_id)
        encoded_client_secret = str(google_result["client_secret"])
        client_secret = decode(encoded_client_secret)
        encoded_refresh_token = str(google_result["refresh_token"])
        refresh_token = decode(encoded_refresh_token)
        google = G(project_id, client_secret, refresh_token)
        google.list_instances(pro_id, zone)
        instance_list = google.list_instances("autum-165318", "us-central1-f")
        instance_db = instance_list

        return render_to_response("google_view.html", {'instance_db': instance_db},
                                  context_instance=RequestContext(request))

def google_delete(request):
    if request.method == 'POST':
        selectzone = str(request.POST.get("selectzone"))
        Pro_id = str(request.POST.get("Pro_id"))
        Inst_name = str(request.POST.get("Inst_name"))
        google_result = google_get_keys(request)
        encoded_project_id = str(google_result["project_id"])
        project_id = decode(encoded_project_id)
        encoded_client_secret = str(google_result["client_secret"])
        client_secret = decode(encoded_client_secret)
        encoded_refresh_token = str(google_result["refresh_token"])
        refresh_token = decode(encoded_refresh_token)
        google = G(project_id, client_secret, refresh_token)
        google.delete_instance(Pro_id,selectzone, Inst_name)
        return render_to_response("google_home.html", {}, context_instance=RequestContext(request))
    return render_to_response("google_delete.html", {}, context_instance=RequestContext(request))


def google_get_keys(request):
    usr_id = request.user.id
    google_result = Google.objects.get(id=usr_id)
    project_id = google_result.project_id
    client_secret = google_result.client_secret
    refresh_token = google_result.refresh_token
    keys = {"project_id": project_id, "client_secret": client_secret, "refresh_token": refresh_token}
    return keys

def google_monitor(request):
    google_result = google_get_keys(request)
    encoded_project_id = str(google_result["project_id"])
    project_id = decode(encoded_project_id)
    encoded_client_secret = str(google_result["client_secret"])
    client_secret = decode(encoded_client_secret)
    encoded_refresh_token = str(google_result["refresh_token"])
    refresh_token = decode(encoded_refresh_token)
    google = G(project_id, client_secret, refresh_token)
    data1 = google.cloud_monitor(project_id)
    return render_to_response("google_monitor.html", {'data1': data1})