from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.db import connection

# Create your views here.
def associate(request):
    associate_id = request.user.id
    if request.method == 'POST':
        first_name = str(request.POST.get("first_name"))
        middle_name = str(request.POST.get("middle_name"))
        last_name = str(request.POST.get("last_name"))
        address = str(request.POST.get("address"))
        print first_name, middle_name, last_name, address
        cursor = connection.cursor()
        # associate = cursor.execute("INSERT INTO associates VALUES (" + associate_id + "," +first_name+ "" +middle_name+ ","+last_name+","+address+")")
    if request.method == 'GET':
        associate_id =1
        cursor = connection.cursor()
        # associate = cursor.execute("SELECT * from associates where associate_id = "+ str(associate_id))
        row = cursor.fetchone()

    return render_to_response("associate.html", {}, context_instance=RequestContext(request))

def associate_schedule(request):
    associate_id = request.user.id
    if request.method == 'POST':
        visit_start_time = str(request.POST.get("visit_start_time"))
        visit_end_time = str(request.POST.get("visit_end_time"))
        room_no = str(request.POST.get("room"))
        cursor = connection.cursor()
        associate = cursor.execute("INSERT INTO inmate_associates_visits VALUES (" + associate_id + "," + visit_start_time + "" + visit_end_time + "," + room + ")")

    return render_to_response("associate_schedule.html", {}, context_instance=RequestContext(request))