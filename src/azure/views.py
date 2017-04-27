from django.shortcuts import render
from django.template import RequestContext
from django.shortcuts import render_to_response
from .forms import AzureForm
<<<<<<< HEAD
from models import Azure
from django.http import HttpResponse
from django.contrib.auth.models import User
import json
import boto
from django.views.generic import TemplateView
from django.http import HttpResponse
=======
from .models import Azure
>>>>>>> 1816083a6388300f524dc9930227be21ad46c8a9


# Create your views here.
# def azure(request):
# 	form = AzureForm()
# 	context ={
# 	"form" : form,
# 	}
# 	return render_to_response("Azure_CP.html", context, context_instance = RequestContext(request))


def azure(request):
<<<<<<< HEAD
    form = AzureForm()
    context = {
        "form": form,
    }
    return render_to_response("Azure_CP.html", context, context_instance=RequestContext(request))
=======
    # Get the user Id of logged in user
    usr_id = request.user.id

    # Mathch the user Id against user_id column of aws table
    try:
        azure_result = Azure.objects.get (user_id=usr_id)
    except:
        azure_result = None

    # If the logged in user Id matches against user_id inside aws table, that means the user has already entered and
    # saved the aws key and secret key in database, therefore the AWS dashboard is shown to user
    if azure_result is not None:
        return render_to_response ("Azure_Home.html", {}, context_instance=RequestContext (request))

    # Else If the user Id does not mataches against user_id of aws table, we will now show the AWS form in which user can
    # save his/her aws credentials
    else:
        # If the request method is POST that means user has filled the form so now the aws key and aws secret of
        # user will be saved in databae
        if request.method == 'POST':
            print "it is post"
            form = AzureForm (request.POST or None)
            if form.is_valid ():
                aws_key = form.cleaned_data['aws_access_key']
                aws_secret = form.cleaned_data['aws_secret_key']
                keys = AWSModel (user_id=usr_id, aws_access_key=aws_key, aws_secret_key=aws_secret)
                save_keys = AWSModel.save (keys)
                print "AWS KEYS HAS BEEN SAVED IN AWS TABLE"
                return render_to_response ("aws_home.html", {}, context_instance=RequestContext (request))
        # Else if the request method is GET that means user is visiting the AWS Signup form, therefore AWS
        # sign up form is shown to the user
        else:
            form = AWSForm ()

            context = {
                "form": form,
            }

            return render_to_response ("AWS_CP.html", context, context_instance=RequestContext (request))
>>>>>>> 1816083a6388300f524dc9930227be21ad46c8a9


def azure_home(request):
    print "azure_home **************************"
<<<<<<< HEAD

    if request.is_ajax():
        print "it's ajax"
    if request.method == 'POST':
        print "I am here inside post"

        selectOP = request.POST.get("selectOP")

        print selectOP

    	return render_to_response("azure_home.html", {}, context_instance=RequestContext(request))
	elif request.method == 'GET':
		return render_to_response("azure_create.html", {})


def azure_create(request):
    print "azure_create **************************"

    if request.is_ajax():
        print "it's ajax"
    if request.method == 'POST':
        print "I am here inside post"

        choice = request.POST.get("choice")
        user = request.POST.get("user")
        password = request.POST.get("pass")
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
	elsif request.method == 'GET':
		return render_to_response("azure_delete.html", {})



def azure_stop(request):
    print "azure_stop **************************"

    if request.is_ajax():
        print "it's ajax"
    if request.method == 'POST':
        print "I am here inside post"

        instance = request.POST.get("instance")

        print instance

    	return render_to_response("azure_stop.html", {}, context_instance=RequestContext(request))

	elif request.method == 'GET':
		return render_to_response("azure_stop.html", {})


def azure_start(request):
    print "azure start **************************"

    if request.is_ajax():
        print "it's ajax"
    if request.method == 'POST':
        print "I am here inside post"

        instance = request.POST.get("instance")

        print instance

    	return render_to_response("azure_start.html", {}, context_instance=RequestContext(request))

	elif request.method == 'GET':
		return render_to_response("azure_start.html", {})


def azure_reboot(request):
    print "azure_reboot **************************"

    if request.is_ajax():
        print "it's ajax"
    if request.method == 'POST':
        print "I am here inside post"

        instance = request.POST.get("instance")

        print instance

    	return render_to_response("azure_reboot.html", {}, context_instance=RequestContext(request))

	elif request.method == 'GET':
		return render_to_response("azure_reboot.html", {})
=======

    if request.is_ajax ():
        print "it's ajax"
    if request.method == 'POST':
        print "I am here inside post"

        selectOP = request.POST.get ("selectOP")

        print selectOP

    return render_to_response ("Azure_Home.html", {}, context_instance=RequestContext (request))
>>>>>>> 1816083a6388300f524dc9930227be21ad46c8a9
