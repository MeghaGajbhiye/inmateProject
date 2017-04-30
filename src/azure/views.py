from django.shortcuts import render
from django.template import RequestContext
from django.shortcuts import render_to_response
from .forms import AzureForm

from models import Azure
from django.http import HttpResponse
from django.contrib.auth.models import User
import json
import boto3
from django.views.generic import TemplateView
from django.http import HttpResponse

from .models import Azure

# Create your views here.
# def azure(request):
# 	form = AzureForm()
# 	context ={
# 	"form" : form,
# 	}
# 	return render_to_response("Azure_CP.html", context, context_instance = RequestContext(request))


def azure(request):

    form = AzureForm()
    context = {
        "form": form,
    }
    return render_to_response("Azure_CP.html", context, context_instance=RequestContext(request))


def azure_home(request):
    print "azure_home **************************"

    if request.is_ajax():
        print "it's ajax"
    if request.method == 'POST':
        print "I am here inside post"

        selectOP = request.POST.get("selectOP")

        print selectOP

    	return render_to_response("azure_home.html", {}, context_instance=RequestContext(request))
    elif request.method == 'GET':
		return render_to_response("azure_home.html", {})


def azure_create(request):
    print "azure_create **************************"

    if request.is_ajax():
        print "it's ajax"
    if request.method == 'POST':
        print "I am here inside post"

        choice = request.POST.get("choice")
        user = request.POST.get("user")
        password = request.POST.get("password")
        res_grp_name = request.POST.get("res_grp_name")
        vm_name = request.POST.get("vm_name")
        loc = request.POST.get("loc")
        vnet_name = request.POST.get("vnet_name")
        snet_name = request.POST.get("snet_name")
        nic_name = request.POST.get("nic_name")
        ip_con = request.POST.get("ip_con")
        d_name = request.POST.get("d_name")

    	print choice, user, password, res_grp_name, vm_name, loc, vnet_name, snet_name, nic_name, ip_con, d_name

    	return render_to_response("azure_create.html", {}, context_instance=RequestContext(request))

    elif request.method == 'GET':
		return render_to_response("azure_create.html", {})


def azure_update(request):
    print "azure_update **************************"

    if request.is_ajax():
        print "it's ajax"

	if request.method == 'POST':
		print "I am here inside post"
		size = request.POST.get("size")
		res_grp_name = request.POST.get("res_grp_name")
		vm_name = request.POST.get("vm_name")
		print size, res_grp_name, vm_name
		return render_to_response("azure_update.html", {}, context_instance=RequestContext(request))
	elif request.method == 'GET':
		return render_to_response("azure_update.html", {})

def azure_delete(request):
    print "azure_delete **************************"

    if request.is_ajax():
        print "it's ajax"
    if request.method == 'POST':
        print "I am here inside post"
        res_grp_name = request.POST.get("res_grp_name")
        vm_name = request.POST.get("vm_name")
        print res_grp_name, vm_name
    	return render_to_response("azure_delete.html", {}, context_instance=RequestContext(request))
    elif request.method == 'GET':
		return render_to_response("azure_delete.html", {})



def azure_stop(request):
    print "azure_stop **************************"

    if request.is_ajax():
        print "it's ajax"
    if request.method == 'POST':
        print "I am here inside post"
        res_grp_name = request.POST.get("res_grp_name")
        vm_name = request.POST.get("vm_name")
        print res_grp_name, vm_name
    	return render_to_response("azure_stop.html", {}, context_instance=RequestContext(request))
    elif request.method == 'GET':
		return render_to_response("azure_stop.html", {})


def azure_start(request):
    print "azure start **************************"

    if request.is_ajax():
        print "it's ajax"
    if request.method == 'POST':
        print "I am here inside post"
        res_grp_name = request.POST.get("res_grp_name")
        vm_name = request.POST.get("vm_name")
        print res_grp_name, vm_name
    	return render_to_response("azure_start.html", {}, context_instance=RequestContext(request))
    elif request.method == 'GET':
		return render_to_response("azure_start.html", {})

def azure_view(request):
    print "azure_view **************************"

    if request.is_ajax():
        print "it's ajax"
    if request.method == 'POST':
        print "I am here inside post"
        res_grp_name = request.POST.get("res_grp_name")

        print res_grp_name
    	return render_to_response("azure_view.html", {}, context_instance=RequestContext(request))
    elif request.method == 'GET':
		return render_to_response("azure_view.html", {})



def azure_reboot(request):
    print "azure_reboot **************************"

    if request.is_ajax():
        print "it's ajax"
    if request.method == 'POST':
        print "I am here inside post"
        res_grp_name = request.POST.get("res_grp_name")
        vm_name = request.POST.get("vm_name")
        print res_grp_name, vm_name
    	return render_to_response("azure_reboot.html", {}, context_instance=RequestContext(request))
    elif request.method == 'GET':
		return render_to_response("azure_reboot.html", {})
