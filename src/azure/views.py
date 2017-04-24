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


def azure_inst(request):
	print "azure_inst **************************"

	if request.is_ajax():
		print "it's ajax"
	if request.method == 'POST':
		print "I am here inside post"

		selectOP = request.POST.get("selectOP")

		print selectOP

	return render_to_response("azure_inst.html", {}, context_instance=RequestContext(request))
