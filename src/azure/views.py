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
    print "azure cp"
    usr_id = request.user.id
    try:
        azure_result = Azure.objects.get(id=usr_id)

    except:
        azure_result = None
        print "user verification done"
    if azure_result is not None:
        print "user registered"
        return render_to_response("azure_home.html", {}, context_instance=RequestContext(request))
    else:
        if request.method == 'POST':
            print "it is post"
            form = AzureForm(request.POST or None)
            if form.is_valid():
                subscription_id = form.cleaned_data['subscription_id']
                client_id = form.cleaned_data['client_id']
                secret_key = form.cleaned_data['secret_key']
                tenant_id = form.cleaned_data['tenant_id']
                print subscription_id, client_id, secret_key, tenant_id
                keys = Azure(id=usr_id, subscription_id=subscription_id, client_id=client_id,
                             secret_key=secret_key, tenant_id=tenant_id, )
                save_keys = Azure.save(keys)
                print "Azure KEYS HAS BEEN SAVED IN Azure TABLE"
                return render_to_response("azure_home.html", {}, context_instance=RequestContext(request))
        else:
            form = AzureForm()
            context = {
            "form": form,
            }
        return render_to_response("Azure_CP.html", context, context_instance=RequestContext(request))
        # elif request.method == 'GET':
            #     return render(request, 'Azure_CP.html', {'form': form})
            #


def azure_home(request):
    print "azure_home **************************"

    if request.is_ajax():
        print "it's ajax"
    if request.method == 'POST':
        print "I am here inside post"

        selectOP = request.POST.get("selectOP")

        print selectOP

        return render_to_response("azure_home.html", {}, context_instance=RequestContext(request))

    return render_to_response("azure_home.html", {}, context_instance=RequestContext(request))

def azure_create(request):
    print "azure_create **************************"

    if request.method == 'GET':
        return render_to_response("azure_create.html", {}, context_instance=RequestContext(request))

    else:
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
        usr_id = request.id
        azure_result = Azure.objects.get(id=usr_id)
        subscription_id = azure_result.subscription_id
        client_id = azure_result.client_id
        secret_key = azure_result.secret_key
        tenant_id = azure_result.tenant_id
        print subscription_id, client_id, secret_key, tenant_id

        # Instantiate AWS class aws->aws.py and calling the launch_instance function
        azure = Azure(subscription_id, client_id, secret_key, tenant_id)

        azure.create_instance(choice, user, password, res_grp_name, vm_name, loc, vnet_name, snet_name, nic_name,
                              ip_con, d_name)

        return render_to_response("azure_home.html", {}, context_instance=RequestContext(request))
    return render_to_response("azure_create.html", {}, context_instance=RequestContext(request))


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
            keys = azure_get_keys(request)
            subscription_id = keys["subscription_id"]
            client_id = keys["client_id"]
            secret_key = keys["secret_key"]
            tenant_id = keys["tenant_id"]
            azure = Azure(subscription_id, client_id, secret_key, tenant_id)
            azure.update_instance(size, res_grp_name, vm_name)
            print "I got the azure keys"
        return render_to_response("azure_home.html", {}, context_instance=RequestContext(request))
    return render_to_response("azure_update.html", {}, context_instance=RequestContext(request))


def azure_delete_vm(request):
    print "azure_delete_vm **************************"

    if request.is_ajax():
        print "it's ajax"
        if request.method == 'POST':
            print "I am here inside post"
            res_grp_name = request.POST.get("res_grp_name")
            vm_name = request.POST.get("vm_name")
            print res_grp_name, vm_name
            keys = azure_get_keys(request)
            subscription_id = keys["subscription_id"]
            client_id = keys["client_id"]
            secret_key = keys["secret_key"]
            tenant_id = keys["tenant_id"]
            azure = Azure(subscription_id, client_id, secret_key, tenant_id)
            azure.delete_vm(res_grp_name, vm_name)
            print "I got the azure keys"
        return render_to_response("azure_home.html", {}, context_instance=RequestContext(request))
    return render_to_response("azure_delete_vm.html", {}, context_instance=RequestContext(request))

# return render_to_response("azure_delete_vm.html", {})



def azure_stop(request):
    print "azure_stop **************************"

    if request.is_ajax():
        print "it's ajax"
        if request.method == 'POST':
            print "I am here inside post"
            res_grp_name = request.POST.get("res_grp_name")
            vm_name = request.POST.get("vm_name")
            print res_grp_name, vm_name
            keys = azure_get_keys(request)
            subscription_id = keys["subscription_id"]
            client_id = keys["client_id"]
            secret_key = keys["secret_key"]
            tenant_id = keys["tenant_id"]
            azure = Azure(subscription_id, client_id, secret_key, tenant_id)
            azure.stop_vm(res_grp_name, vm_name)
            print "I got the azure keys"
        return render_to_response("azure_home.html", {}, context_instance=RequestContext(request))
    return render_to_response("azure_stop.html", {}, context_instance=RequestContext(request))



def azure_start(request):
    print "azure start **************************"

    if request.is_ajax():
        print "it's ajax"
    if request.method == 'POST':
        print "I am here inside post"
        res_grp_name = request.POST.get("res_grp_name")
        vm_name = request.POST.get("vm_name")
        print res_grp_name, vm_name
        keys = azure_get_keys(request)
        subscription_id = keys["subscription_id"]
        client_id = keys["client_id"]
        secret_key = keys["secret_key"]
        tenant_id = keys["tenant_id"]
        azure = Azure(subscription_id, client_id, secret_key, tenant_id)
        azure.start_vm(res_grp_name, vm_name)
        print "I got the azure keys"

        # print res_grp_name, vm_name
        return render_to_response("azure_home.html", {}, context_instance=RequestContext(request))
    return render_to_response("azure_start.html", {}, context_instance=RequestContext(request))


def azure_view(request):
    print "azure_view **************************"

    if request.is_ajax():
        print "it's ajax"
    if request.method == 'POST':
        print "I am here inside post"
        res_grp_name = request.POST.get("res_grp_name")
        keys = azure_get_keys(request)
        print res_grp_name
        subscription_id = keys["subscription_id"]
        client_id = keys["client_id"]
        secret_key = keys["secret_key"]
        tenant_id = keys["tenant_id"]
        azure = Azure(subscription_id, client_id, secret_key, tenant_id)
        azure.view_instances(res_grp_name)
        print "I got the azure keys"

        # print res_grp_name
        return render_to_response("azure_home.html", {}, context_instance=RequestContext(request))
    return render_to_response("azure_view.html", {}, context_instance=RequestContext(request))


# elif request.method == 'GET':
# return render_to_response("azure_view.html", {})



def azure_reboot(request):
    print "azure_reboot **************************"

    if request.is_ajax():
        print "it's ajax"
    if request.method == 'POST':
        print "I am here inside post"
        res_grp_name = request.POST.get("res_grp_name")
        vm_name = request.POST.get("vm_name")
        print res_grp_name, vm_name
        keys = azure_get_keys(request)
        subscription_id = keys["subscription_id"]
        client_id = keys["client_id"]
        secret_key = keys["secret_key"]
        tenant_id = keys["tenant_id"]
        azure = Azure(subscription_id, client_id, secret_key, tenant_id)
        azure.restart_vm(res_grp_name, vm_name)
        print "I got the azure keys"
        return render_to_response("azure_home.html", {}, context_instance=RequestContext(request))
    # print res_grp_name, vm_name
    return render_to_response("azure_reboot.html", {}, context_instance=RequestContext(request))


#   elif request.method == 'GET':
# return render_to_response("azure_reboot.html", {})

def azure_get_keys(request):
    print "get azure keys"
    usr_id = request.id
    azure_result = Azure.objects.get(id=usr_id)
    subscription_id = azure_result.subscription_id
    client_id = azure_result.client_id
    secret_key = azure_result.secret_key
    tenant_id = azure_result.tenant_id
    print subscription_id, client_id, secret_key, tenant_id
    keys = {"subscription_id": subscription_id, "client_id": client_id, "secret_key": secret_key,
            "tenant_id": tenant_id}
    return keys
