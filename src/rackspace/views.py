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
	return render_to_response("rackspace.html", context, context_instance = RequestContext(request))

def rackspace_home(request):
    print "rackspace_home **************************"

    if request.is_ajax():
        print "it's ajax"
    if request.method == 'POST':
        print "I am here inside post"
        instance = request.POST.get("instance")
        selectram = request.POST.get("selectram")
        selectimage = request.POST.get("selectimage")
        print instance, selectram, selectimage
    return render_to_response("rackspace_home.html", {}, context_instance = RequestContext(request))
