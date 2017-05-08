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
import base64


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
def google(request):
    print "google cp****"
    usr_id = request.user.id
    try:
        google_result = Google.objects.get(id=usr_id)
    except:
        google_result = None
    if google_result is not None:
        return render_to_response("google_home.html", {}, context_instance=RequestContext(request))
    else:
        if request.method == 'POST':
           print "it is post"
           form = GoogleForm(request.POST or None)
           if form.is_valid():
               project_id = form.cleaned_data['project_id']
               client_secret = form.cleaned_data['client_secret']
               refresh_token = form.cleaned_data['refresh_token']
               keys = Google(id=usr_id, project_id=project_id, client_secret=client_secret, refresh_token=refresh_token)
               save_keys = Google.save(keys)
               print "Google KEYS HAS BEEN SAVED IN Google TABLE"
               return render_to_response("google_home.html", {}, context_instance=RequestContext(request))
        else:
            form = GoogleForm()
            context = {
                "form": form,
            }
            return render_to_response("Google_CP.html", context, context_instance=RequestContext(request))



def google_home(request):
    print "google_home **************************"

    if request.is_ajax():
        print "it's ajax"
    if request.method == 'POST':
        print "I am here inside post"
        selectOP = request.POST.get("selectOP")
        print selectOP
    return render_to_response("google_home.html", {}, context_instance=RequestContext(request))


def google_create(request):
    print "google_create **************************"

    if request.method == 'GET':

        return render_to_response("google_create.html", {}, context_instance=RequestContext(request))
    else:
        if request.method == 'POST':
            print "I am here inside post"
            selectzone = request.POST.get("selectzone")
            Pro_id = request.POST.get("Pro_id")
            Buck_id = request.POST.get("Buck_id")
            Inst_name = request.POST.get("Inst_name")
            print selectzone, Pro_id, Buck_id, Inst_name
            usr_id = request.user.id
            google_result = Google.objects.get(id=usr_id)
            project_id = google_result.project_id
            client_secret = google_result.client_secret
            refresh_token = google_result.refresh_token
            print project_id, client_secret, refresh_token
            google = Google(project_id, client_secret, refresh_token)
            google.create_instance(selectzone, Pro_id, Buck_id, Inst_name)
            return render_to_response("google_home.html", {}, context_instance=RequestContext(request))
    return render_to_response("google_create.html", {}, context_instance=RequestContext(request))


def google_retrieve(request):
    print "google_retrieve **************************"

    if request.is_ajax():
        print "it's ajax"
    if request.method == 'POST':
        print "I am here inside post"
        selectzone = request.POST.get("selectzone")
        Pro_id = request.POST.get("Pro_id")
        keys = google_get_keys(request)
        print keys
        project_id = keys["project_id"]
        client_secret = keys["client_secret"]
        refresh_token = keys["refresh_token"]
        google = Google(project_id, client_secret, refresh_token)
        google.list_instances(selectzone, Pro_id)
        # print selectzone, Pro_id
        return render_to_response("google_home.html", {}, context_instance=RequestContext(request))
    return render_to_response("google_retrieve.html", {}, context_instance=RequestContext(request))


def google_delete(request):
    print "google_delete **************************"

    if request.is_ajax():
        print "it's ajax"
    if request.method == 'POST':
        print "I am here inside post"
        selectzone = request.POST.get("selectzone")
        Pro_id = request.POST.get("Pro_id")
        Inst_name = request.POST.get("Inst_name")
        keys = google_get_keys(request)
        project_id = keys["project_id"]
        client_secret = keys["client_secret"]
        refresh_token = keys["refresh_token"]
        google = Google(project_id, client_secret, refresh_token)
        google.delete_instance(selectzone, Pro_id, Inst_name)
        # print selectzone, Pro_id, Inst_name
        return render_to_response("google_home.html", {}, context_instance=RequestContext(request))
    return render_to_response("google_delete.html", {}, context_instance=RequestContext(request))


def google_get_keys(request):
    usr_id = request.user.id
    google_result = Google.objects.get(id=usr_id)
    project_id = google_result.project_id
    client_secret = google_result.project_id
    refresh_token = google_result.project_id
    print project_id, client_secret, refresh_token
    keys = {"project_id": project_id, "client_secret": client_secret, "refresh_token": refresh_token}
    return keys

def google_monitor(request):
    data1 = [['2015-05-01 T 17:23:00', 45235.0], ['2015-05-01 T 19:23:00', 56535.0]]
    return render_to_response("google_monitor.html", {'data1': data1})