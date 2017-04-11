from django.shortcuts import render
from django.template import RequestContext
from django.shortcuts import render_to_response
from .forms import GoogleForm
# Create your views here.
def google(request):
	form =GoogleForm()
	context = {
	"form" : form,
	}
	return render_to_response("Google_CP.html", context, context_instance = RequestContext(request))
