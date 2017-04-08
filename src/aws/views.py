from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from models import AWS
from .forms import AWSForm
import boto

def aws(request):
	form = AWSForm()
	context = {
	"form" : form,
	}
	return render_to_response("AWS_CP.html", context, context_instance = RequestContext(request))
	
# Create your views here.

def aws_home(request):
	user_id = request.user.id
	print user_id
	aws_model = AWS()
	print aws_model.all()
	# user_Data = request.user_Data
	jsonList = []
	aws_access_key_id = 'AKIAJKLGF55A33R3KTMQ'
	aws_secret_access_key = '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'
	ec2 = boto.connect_ec2(aws_access_key_id=aws_access_key_id,
	aws_secret_access_key=aws_secret_access_key)
	parsed_data = []
	user_Data = {}
	# checking all zones
	data	= list(ec2.get_all_zones())
	context = {
	"data" : data, 
	}
	return render_to_response("AWS_Home.html", context, context_instance = RequestContext(request))
