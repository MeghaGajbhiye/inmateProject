from django.shortcuts import render
from django.template import RequestContext
from django.shortcuts import render_to_response
from .forms import AzureForm
from models import Azure
from django.http import HttpResponse
from django.contrib.auth.models import User
import json
from django.views.generic import TemplateView
from django.http import HttpResponse
from azure_python import Azure_class as az
import base64

# Create your views here.
# def azure(request):
# 	form = AzureForm()
# 	context ={
# 	"form" : form,
# 	}
# 	return render_to_response("Azure_CP.html", context, context_instance = RequestContext(request))

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

def azure_cp(request):
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
                encoded_subscription_id = encode(subscription_id)
                client_id = form.cleaned_data['client_id']
                encoded_client_id = encode(client_id)
                secret_key = form.cleaned_data['secret_key']
                encoded_secret_key = encode(secret_key)
                tenant_id = form.cleaned_data['tenant_id']
                encoded_tenant_id = encode(tenant_id)
                print subscription_id, client_id, secret_key, tenant_id
                keys = Azure(id=usr_id, subscription_id=encoded_subscription_id, client_id=encoded_client_id,
                             secret_key=encoded_secret_key, tenant_id=encoded_tenant_id, )
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
            
            azure_result = azure_get_keys(request)
            encoded_subscription_id = str(azure_result["subscription_id"])
            subscription_id = decode(encoded_subscription_id)
            encoded_client_id = str(azure_result["client_id"])
            client_id = decode(encoded_client_id)
            encoded_secret_key = str(azure_result["secret_key"])
            secret_key = decode(encoded_secret_key)
            encoded_tenant_id = str(azure_result["tenant_id"])
            tenant_id = decode(encoded_tenant_id)
            print subscription_id, client_id, secret_key, tenant_id
            azure = az(subscription_id, client_id, secret_key, tenant_id)

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
            azure_result = azure_get_keys(request)
            encoded_subscription_id = str(azure_result["subscription_id"])
            subscription_id = decode(encoded_subscription_id)
            encoded_client_id = str(azure_result["client_id"])
            client_id = decode(encoded_client_id)
            encoded_secret_key = str(azure_result["secret_key"])
            secret_key = decode(encoded_secret_key)
            encoded_tenant_id = str(azure_result["tenant_id"])
            tenant_id = decode(encoded_tenant_id)
            print subscription_id, client_id, secret_key, tenant_id
            azure = az(subscription_id, client_id, secret_key, tenant_id)
            azure.update_instance(size, res_grp_name, vm_name)
            print "I got the azure keys"
        return render_to_response("azure_home.html", {}, context_instance=RequestContext(request))
    return render_to_response("azure_update.html", {}, context_instance=RequestContext(request))

def azure_delete(request):
    print "azure_delete **************************"

    if request.is_ajax():
        print "it's ajax"
        if request.method == 'POST':
            print "I am here inside post"
            selectOP = request.POST.get("selectOP")

            print selectOP
            azure_result = azure_get_keys(request)
            encoded_subscription_id = str(azure_result["subscription_id"])
            subscription_id = decode(encoded_subscription_id)
            encoded_client_id = str(azure_result["client_id"])
            client_id = decode(encoded_client_id)
            encoded_secret_key = str(azure_result["secret_key"])
            secret_key = decode(encoded_secret_key)
            encoded_tenant_id = str(azure_result["tenant_id"])
            tenant_id = decode(encoded_tenant_id)
            print subscription_id, client_id, secret_key, tenant_id
            azure = az(subscription_id, client_id, secret_key, tenant_id)


        return render_to_response("azure_delete.html", {}, context_instance=RequestContext(request))
    return render_to_response("azure_delete.html", {}, context_instance=RequestContext(request))

def azure_delete_vm(request):
    print "azure_delete_vm **************************"

    if request.is_ajax():
        print "it's ajax"
        if request.method == 'POST':
            print "I am here inside post"
            res_grp_name = request.POST.get("res_grp_name")
            vm_name = request.POST.get("vm_name")
            print res_grp_name, vm_name
            azure_result = azure_get_keys(request)
            encoded_subscription_id = str(azure_result["subscription_id"])
            subscription_id = decode(encoded_subscription_id)
            encoded_client_id = str(azure_result["client_id"])
            client_id = decode(encoded_client_id)
            encoded_secret_key = str(azure_result["secret_key"])
            secret_key = decode(encoded_secret_key)
            encoded_tenant_id = str(azure_result["tenant_id"])
            tenant_id = decode(encoded_tenant_id)
            print subscription_id, client_id, secret_key, tenant_id
            azure = az(subscription_id, client_id, secret_key, tenant_id)
            azure.delete_vm(res_grp_name, vm_name)
            instance_db = [u'instance_test', u'Server-02', u'vm1']
            print "I am above instance_name"
            instance_name = json.dumps(instance_db)
            print instance_name
            context = {"instance_name": instance_name}
            print "Gotcha instance"
            return render_to_response("azure_delete_vm.html", {}, context_instance=RequestContext(request))
    elif request.method == 'GET':
        instance_db = [u'instance_test', u'Server-02', u'vm1']
        return render_to_response("azure_delete_vm.html", {'instance_db': instance_db})
# return render_to_response("azure_delete_vm.html", {})

def azure_delete_rsgrp(request):
    print "azure_delete_rsgrp **************************"

    if request.is_ajax():
        print "it's ajax"
        if request.method == 'POST':
            print "I am here inside post"
            res_grp_name = request.POST.get("res_grp_name")
            print res_grp_name
            azure_result = azure_get_keys(request)
            encoded_subscription_id = str(azure_result["subscription_id"])
            subscription_id = decode(encoded_subscription_id)
            encoded_client_id = str(azure_result["client_id"])
            client_id = decode(encoded_client_id)
            encoded_secret_key = str(azure_result["secret_key"])
            secret_key = decode(encoded_secret_key)
            encoded_tenant_id = str(azure_result["tenant_id"])
            tenant_id = decode(encoded_tenant_id)
            print subscription_id, client_id, secret_key, tenant_id
            azure = az(subscription_id, client_id, secret_key, tenant_id)
            azure.delete_vm(res_grp_name)
            print "I got the azure keys"
        return render_to_response("azure_home.html", {}, context_instance=RequestContext(request))
    return render_to_response("azure_delete_rsgrp.html", {}, context_instance=RequestContext(request))


def azure_stop(request):
    print "azure_stop **************************"

    if request.is_ajax():
        print "it's ajax"
        if request.method == 'POST':
            print "I am here inside post"
            res_grp_name = request.POST.get("res_grp_name")
            vm_name = request.POST.get("vm_name")
            print res_grp_name, vm_name
            azure_result = azure_get_keys(request)
            encoded_subscription_id = str(azure_result["subscription_id"])
            subscription_id = decode(encoded_subscription_id)
            encoded_client_id = str(azure_result["client_id"])
            client_id = decode(encoded_client_id)
            encoded_secret_key = str(azure_result["secret_key"])
            secret_key = decode(encoded_secret_key)
            encoded_tenant_id = str(azure_result["tenant_id"])
            tenant_id = decode(encoded_tenant_id)
            print subscription_id, client_id, secret_key, tenant_id
            azure = az(subscription_id, client_id, secret_key, tenant_id)
            az.stop_vm(res_grp_name, vm_name)
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
        azure_result = azure_get_keys(request)
        encoded_subscription_id = str(azure_result["subscription_id"])
        subscription_id = decode(encoded_subscription_id)
        encoded_client_id = str(azure_result["client_id"])
        client_id = decode(encoded_client_id)
        encoded_secret_key = str(azure_result["secret_key"])
        secret_key = decode(encoded_secret_key)
        encoded_tenant_id = str(azure_result["tenant_id"])
        tenant_id = decode(encoded_tenant_id)
        print subscription_id, client_id, secret_key, tenant_id
        azure = az(subscription_id, client_id, secret_key, tenant_id)
        az.start_vm(res_grp_name, vm_name)
        
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
        azure_result = azure_get_keys(request)
        encoded_subscription_id = str(azure_result["subscription_id"])
        subscription_id = decode(encoded_subscription_id)
        encoded_client_id = str(azure_result["client_id"])
        client_id = decode(encoded_client_id)
        encoded_secret_key = str(azure_result["secret_key"])
        secret_key = decode(encoded_secret_key)
        encoded_tenant_id = str(azure_result["tenant_id"])
        tenant_id = decode(encoded_tenant_id)
        print subscription_id, client_id, secret_key, tenant_id
        azure = az(subscription_id, client_id, secret_key, tenant_id)
        az.view_instances(res_grp_name)
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
        azure_result = azure_get_keys(request)
        print "I got the azure keys"
        encoded_subscription_id = str(azure_result["subscription_id"])
        subscription_id = decode(encoded_subscription_id)
        encoded_client_id = str(azure_result["client_id"])
        client_id = decode(encoded_client_id)
        encoded_secret_key = str(azure_result["secret_key"])
        secret_key = decode(encoded_secret_key)
        encoded_tenant_id = str(azure_result["tenant_id"])
        tenant_id = decode(encoded_tenant_id)
        print subscription_id, client_id, secret_key, tenant_id
        azure = az(subscription_id, client_id, secret_key, tenant_id)
        az.restart_vm(res_grp_name, vm_name)
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

def azure_monitor(request):
    azure_result = azure_get_keys(request)
    print "I got the azure keys"
    encoded_subscription_id = str(azure_result["subscription_id"])
    subscription_id = decode(encoded_subscription_id)
    encoded_client_id = str(azure_result["client_id"])
    client_id = decode(encoded_client_id)
    encoded_secret_key = str(azure_result["secret_key"])
    secret_key = decode(encoded_secret_key)
    encoded_tenant_id = str(azure_result["tenant_id"])
    tenant_id = decode(encoded_tenant_id)
    print subscription_id, client_id, secret_key, tenant_id

        # Instantiate azure class
    azure = az(subscription_id, client_id, secret_key, tenant_id)    
    time = ['2017 - 04 - 29 00:00:00 + 00:00', '2017 - 04 - 29 01:00:00 + 00:00']
    zone = [None, None]
    data = zip(time,zone)
    return render_to_response("azure_monitor.html", {'data':data})
