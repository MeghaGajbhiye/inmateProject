from django.shortcuts import render
from django.template import RequestContext
from django.shortcuts import render_to_response
from models import Google
from .forms import GoogleForm
from django.http import HttpResponse
from django.contrib.auth.models import User
import json
import boto
from django.views.generic import TemplateView
from django.http import HttpResponse


# Create your views here.
def google(request):
    form = GoogleForm()
    context = {
        "form": form,
    }
    return render_to_response("Google_CP.html", context, context_instance=RequestContext(request))


def google_create(request):
    print "google_create **************************"

    if request.is_ajax():
        print "it's ajax"
    if request.method == 'POST':
        print "I am here inside post"
        selectzone = request.POST.get("selectzone")
        Pro_id = request.POST.get("Pro_id")
        Buck_id = request.POST.get("Buck_id")
        Inst_name = request.POST.get("Inst_name")
        print selectzone, Pro_id, Buck_id, Inst_name
    return render_to_response("google_create.html", {}, context_instance=RequestContext(request))
    # elif request.method == 'GET':
    #     print "in get method"
    #     return render_to_response("google_create.html", {})

def google_retrieve(request):
    print "google_retrieve **************************"

    if request.is_ajax():
        print "it's ajax"
    if request.method == 'POST':
        print "I am here inside post"
        selectzone = request.POST.get("selectzone")
        Pro_id = request.POST.get("Pro_id")
        print selectzone, Pro_id
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
        print selectzone, Pro_id, Inst_name
    return render_to_response("google_delete.html", {}, context_instance=RequestContext(request))

def google_home(request):
	print "google_home **************************"

	if request.is_ajax():
		print "it's ajax"
	if request.method == 'POST':
		print "I am here inside post"

		selectOP = request.POST.get("selectOP")

		print selectOP

	return render_to_response("google_home.html", {}, context_instance=RequestContext(request))
