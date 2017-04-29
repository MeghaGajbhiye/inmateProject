from django.shortcuts import render
from django.template import RequestContext
from django.shortcuts import render_to_response
from .forms import IBMForm
from models import IBM
from django.http import HttpResponse
from django.contrib.auth.models import User
import json
import boto
from django.views.generic import TemplateView
from django.http import HttpResponse


# Create your views here.
def ibm(request):
	form = IBMForm()
	context = {
	"form" : form,
	}
	return render_to_response("IBM_CP.html", context, context_instance = RequestContext(request))

def ibm_home(request):
    print "ibm_home **************************"
    # if request.method == 'POST':
    # user_id = request.user.id
    # print user_id
    # # aws_model = AWS()
    # # print aws_model.all()
    # aws_access_key_id = ''
    # aws_secret_access_key = ''
    # ec2 = boto.connect_ec2(aws_access_key_id=aws_access_key_id,
    # aws_secret_access_key=aws_secret_access_key)
    # parsed_data = []
    # user_Data = {}
    # # checking all zones
    # # data   = list(ec2.get_all_zones())
    # list_data = list(boto.ec2.regions())
    # # dict_data = dict(list_data)
    # # print list_data
    # list_data = [(1, 'region1'), (2, 'region2'), (3,'region3')]
    # # data = {key: i for i , key in enumerate(list_data)}
    # form = AWSHomeForm(my_choices = list_data)
    # context = {
    # "form" : form,
    # }
    # aws_get_keys()
    # test = request.POST.get("zone", "region", "image", "min_count", "max_count", "key_name", "inst_type", "monitoring")
    if request.is_ajax():
        print "it's ajax"
    if request.method == 'POST':
        print "I am here inside post"

        selectOP = request.POST.get("selectOP")

        print selectOP

    return render_to_response("ibm_home.html", {}, context_instance = RequestContext(request))
    # return HttpResponse(json.dumps(response_data),content_type="application/json")
