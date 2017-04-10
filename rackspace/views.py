from django.shortcuts import render
from django.template import RequestContext
from django.shortcuts import render_to_response
from .forms import RackspaceForm

# Create your views here.
def rackspace(request):
	form = RackspaceForm()
	context = {
	"form" : form,
	}
	return render_to_response("Rackspace.html", context, context_instance = RequestContext(request))
