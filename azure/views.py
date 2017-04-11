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