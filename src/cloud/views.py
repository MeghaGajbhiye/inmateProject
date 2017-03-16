from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
from .forms import SignUpForm
from django.template import RequestContext
from .forms import ContactForm, SignUpForm
from django.conf import settings
from django.core.mail import send_mail

# Create your views here.

def home(request):
	title = "Welcome"
	if request.user.is_authenticated():
		# title = "My title %s" %(request.user)
		title = "Login"
	if request.method == "POST":
		print request.POST
	form = SignUpForm(request.POST or None)
	context = {
	"template_title": title,
	"form": form,}

	if form.is_valid():
		# form.save()
		print request.POST['email'] # not recommended
		instance = form.save(commit = False)
		full_name = form.cleaned_data.get("full_name")

		# print instance.email
		# print instance.full_name
		if not full_name:
			full_name = "MeghaNew"
		instance.full_name = full_name  
		instance.save()
		context = {
			"template_title": "Thank You!"
		}
	# return request(request, "home.html", {})
	# return request(request,"home.html",{})
	# return HttpResponse('My first view.')
	return render_to_response("home.html", context, context_instance=RequestContext(request))




def contact(request):
	form = ContactForm(request.POST or None)
	if form.is_valid(): 
		form_email = form.cleaned_data.get("email")
		form_message=form.cleaned_data.get("message")
		form_full_name = form.cleaned_data.get("full_name")
		print form_message, form_email, form_full_name
		subject = "test"
		from_email = settings.EMAIL_HOST_USER
		to_email = [from_email, "nikki.gajbhiye@gmail.com"]
		contact_message="%s %s via %s "%(form_full_name, form_message, form_email)
		send_mail(subject, contact_message, from_email, to_email, fail_silently = False)
	# 	print email
	# if form.is_valid():
	# 	for key in form.cleaned_data:
	# 		print key, form.cleaned_data.get(key)
		# for key, value in form.cleaned_data.iteritems():
		# 	print key, value
	context = {
	"form" : form, 
	}
	return render_to_response("forms.html", context,context_instance=RequestContext(request))



def dashboard(request):
	return render_to_response("Dash_2.html",)

def aws(request):
	return render_to_response("AWS_CP.html",)

def azure(request):
	return render_to_response("Azure_CP.html",)

def google(request):
	return render_to_response("Google_CP.html",)

def ibm(request):
	return render_to_response("IBM_CP.html",)

def rackspace(request):
	return render_to_response("Rackspace.html",)
