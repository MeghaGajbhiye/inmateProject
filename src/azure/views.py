from django.shortcuts import render
from django.template import RequestContext
from django.shortcuts import render_to_response
from .forms import AzureForm
from .models import Azure


# Create your views here.
# def azure(request):
# 	form = AzureForm()
# 	context ={
# 	"form" : form,
# 	}
# 	return render_to_response("Azure_CP.html", context, context_instance = RequestContext(request))


def azure(request):
    # Get the user Id of logged in user
    usr_id = request.user.id

    # Mathch the user Id against user_id column of aws table
    try:
        azure_result = Azure.objects.get (user_id=usr_id)
    except:
        azure_result = None

    # If the logged in user Id matches against user_id inside aws table, that means the user has already entered and
    # saved the aws key and secret key in database, therefore the AWS dashboard is shown to user
    if azure_result is not None:
        return render_to_response ("Azure_Home.html", {}, context_instance=RequestContext (request))

    # Else If the user Id does not mataches against user_id of aws table, we will now show the AWS form in which user can
    # save his/her aws credentials
    else:
        # If the request method is POST that means user has filled the form so now the aws key and aws secret of
        # user will be saved in databae
        if request.method == 'POST':
            print "it is post"
            form = AzureForm (request.POST or None)
            if form.is_valid ():
                aws_key = form.cleaned_data['aws_access_key']
                aws_secret = form.cleaned_data['aws_secret_key']
                keys = AWSModel (user_id=usr_id, aws_access_key=aws_key, aws_secret_key=aws_secret)
                save_keys = AWSModel.save (keys)
                print "AWS KEYS HAS BEEN SAVED IN AWS TABLE"
                return render_to_response ("aws_home.html", {}, context_instance=RequestContext (request))
        # Else if the request method is GET that means user is visiting the AWS Signup form, therefore AWS
        # sign up form is shown to the user
        else:
            form = AWSForm ()

            context = {
                "form": form,
            }

            return render_to_response ("AWS_CP.html", context, context_instance=RequestContext (request))


def azure_home(request):
    print "azure_home **************************"

    if request.is_ajax ():
        print "it's ajax"
    if request.method == 'POST':
        print "I am here inside post"

        selectOP = request.POST.get ("selectOP")

        print selectOP

    return render_to_response ("Azure_Home.html", {}, context_instance=RequestContext (request))
