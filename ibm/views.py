from django.shortcuts import render
from django.template import RequestContext
from django.shortcuts import render_to_response
from .forms import IBMForm

# Create your views here.
def ibm(request):
	form = IBMForm()
	context = {
	"form" : form,
	}
	return render_to_response("IBM_CP.html", context, context_instance = RequestContext(request))
