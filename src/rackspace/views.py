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


# Create your views here.
def rackspace(request):
    usr_id = request.user.id
    try:
        rackspace_result = Rackspace.objects.get(user_id=usr_id)
    except:
        rackspace_result = None
    if rackspace_result is not None:
        return render_to_response("rackspace_home.html", {}, context_instance=RequestContext(request))
    else:
        if request.method == 'POST':
            print "it is post"
            form = RackspaceForm(request.POST or None)
            if form.is_valid():
                tenant_id = form.cleaned_data['tenant_id']
                keys = Rackspace(user_id=usr_id, )
                save_keys = Rackspace.save(keys)
                print "Rackspace KEYS HAS BEEN SAVED IN Rackspace TABLE"
                return render_to_response("rackspace_home.html", {}, context_instance=RequestContext(request))
                form = RackspaceForm()
                context = {
                    "form": form,
                }
                return render_to_response("rackspace.html", context, context_instance=RequestContext(request))


def rackspace_create(request):
    print "rackspace_create **************************"
    # if request.is_ajax():
    #     print "it's ajax"
    if request.method == 'GET':
        return render_to_response("rackspace_create.html", {}, context_instance=RequestContext(request))
    if request.method == 'POST':
        print "I am here inside post"
        instance = request.POST.get("instance")
        selectram = request.POST.get("selectram")
        selectimage = request.POST.get("selectimage")
        print instance, selectram, selectimage
        usr_id = request.user.id
        rackspace_result = Rackspace.objects.get(user_id=usr_id)
        tenant_id = rackspace_result.tenant_id
        print tenant_id
        rackspace = Rackspace(tenant_id)
        rackspace.launch_instance(instance, selectram, selectimage)
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
    elif request.method == 'GET':
        return render_to_response("rackspace_home.html", {})


def rackspace_update(request):
    print "rackspace_update **************************"
    if request.is_ajax():
        print "it's ajax"
    if request.method == 'GET':
        return render_to_response("rackspace_update.html", {}, context_instance=RequestContext(request))
    if request.method == 'POST':
        print "I am here inside post"
        selectram = request.POST.get("selectram")
        server = request.POST.get("server")
        keys = rackspace_get_keys(request)
        print keys
        tenant_id = keys["tenant_id"]
        rackspace = Rackspace(tenant_id)
        rackspace.update_instance(selectram, server)
        # print selectram, server
        return render_to_response("rackspace_home.html", {}, context_instance=RequestContext(request))
        # elif request.method == 'GET':
        #     return render_to_response("rackspace_update.html", {})


def rackspace_delete(request):
    print "rackspace_update **************************"
    if request.is_ajax():
        print "it's ajax"
    if request.method == 'GET':
        return render_to_response("rackspace_delete.html", {}, context_instance=RequestContext(request))
    if request.method == 'POST':
        print "I am here inside post"
        server = request.POST.get("server")
        keys = rackspace_get_keys(request)
        print keys
        tenant_id = keys["tenant_id"]
        rackspace = Rackspace(tenant_id)
        rackspace.delete_instance(server)
        # print server
        return render_to_response("rackspace_home.html", {}, context_instance=RequestContext(request))
        # elif request.method == 'GET':
        #     return render_to_response("rackspace_delete.html", {})


def rackspace_reboot(request):
    print "rackspace_reboot **************************"
    if request.is_ajax():
        print "it's ajax"
    if request.method == 'GET':
        return render_to_response("rackspace_reboot.html", {}, context_instance=RequestContext(request))
    if request.method == 'POST':
        print "I am here inside post"
        server = request.POST.get("server")
        boot = request.POST.get("boot")
        keys = rackspace_get_keys(request)
        print keys
        tenant_id = keys["tenant_id"]
        rackspace = Rackspace(tenant_id)
        rackspace.instance_reboot(server, boot)
        # print server, boot
        return render_to_response("rackspace_home.html", {}, context_instance=RequestContext(request))
        # elif request.method == 'GET':
        #     return render_to_response("rackspace_reboot.html", {})


def rackspace_view(request):
    print "rackspace_view **************************"
    if request.is_ajax():
        print "it's ajax"
    if request.method == 'GET':
        return render_to_response("rackspace_view.html", {}, context_instance=RequestContext(request))
    if request.method == 'POST':
        print "I am here inside post"
        server_name = request.POST.get("server_name")
        server_ip = request.POST.get("server_ip")
        keys = rackspace_get_keys(request)
        print keys
        tenant_id = keys["tenant_id"]
        rackspace = Rackspace(tenant_id)
        rackspace.view_instance(server_name, server_ip)
        # print server_name, server_ip
        return render_to_response("rackspace_home.html", {}, context_instance=RequestContext(request))
        # elif request.method == 'GET':
        #     return render_to_response("rackspace_view.html", {})


def rackspace_get_keys(request):
    usr_id = request.user.id
    rackspace_result = Rackspace.objects.get(user_id=usr_id)
    tenant_id = rackspace_result.tenant_id
    print tenant_id
    keys = {"tenant_id": tenant_id}
    return keys
