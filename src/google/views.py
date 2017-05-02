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
               keys = Google(id=usr_id, project_id=project_id)
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
            print project_id
            google = Google(project_id)
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
        google = Google(project_id)
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
        google = Google(project_id)
        google.delete_instance(selectzone, Pro_id, Inst_name)
        # print selectzone, Pro_id, Inst_name
        return render_to_response("google_home.html", {}, context_instance=RequestContext(request))
    return render_to_response("google_delete.html", {}, context_instance=RequestContext(request))


def google_get_keys(request):
    usr_id = request.user.id
    google_result = Google.objects.get(id=usr_id)
    project_id = google_result.project_id
    print project_id
    keys = {"project_id": project_id}
    return keys

def google_monitor(request):
    return render_to_response("google_monitor.html", )