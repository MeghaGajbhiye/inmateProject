from django.shortcuts import render
from django.template import RequestContext
from django.shortcuts import render_to_response
from .forms import AzureForm

# Create your views here.
def azure(request):
	form = AzureForm()
	context ={
	"form" : form,
	}
	return render_to_response("Azure_CP.html", context, context_instance = RequestContext(request))


def azure_home(request):
	print "azure_home **************************"

	if request.is_ajax():
		print "it's ajax"
	if request.method == 'POST':
		print "I am here inside post"

		selectOP = request.POST.get("selectOP")

		print selectOP

	return render_to_response("azure_home.html", {}, context_instance=RequestContext(request))

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
		vm_name= request.POST.get("vm_name")
		loc = request.POST.get("loc")
		vnet_name = request.POST.get("vnet_name")
		snet_name = request.POST.get("snet_name")
		nic_name = request.POST.get("nic_name")
		ip_con = request.POST.get("ip_con")
		d_name = request.POST.get("d_name")


		print choice, user, password, res_grp_name, vm_name, loc, vnet_name, snet_name, nic_name, ip_con, d_name

	return render_to_response("azure_create.html", {}, context_instance=RequestContext(request))

def azure_update(request):
	print "azure_update **************************"

	if request.is_ajax():
		print "it's ajax"
	if request.method == 'POST':
		print "I am here inside post"

		size = request.POST.get("size")
		res_grp_name = request.POST.get("res_grp_name")
		vm_name= request.POST.get("vm_name")



		print size, res_grp_name, vm_name

	return render_to_response("azure_create.html", {}, context_instance=RequestContext(request))

def azure_delete(request):
	print "azure_delete **************************"

	if request.is_ajax():
		print "it's ajax"
	if request.method == 'POST':
		print "I am here inside post"

		res_grp_name = request.POST.get("res_grp_name")
		vm_name= request.POST.get("vm_name")



		print res_grp_name, vm_name

	return render_to_response("azure_create.html", {}, context_instance=RequestContext(request))