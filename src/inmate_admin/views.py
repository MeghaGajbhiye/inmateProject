from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.db import connection
import datetime

def inmate(request):
    if request.method == 'GET':
        cursor = connection.cursor()
        inmate = cursor.execute("SELECT inmate_id, inmate_firstname from inmate")
        row = cursor.fetchall()
        inmate_list= []
        for i in row:
            inmate_list.append(i)
        print inmate_list
        return render_to_response("inmate.html", {'inmate': inmate}, context_instance=RequestContext(request))

def associate_inmate(request):
    if request.method == 'GET':
        associate_id = str(request.POST.get("associate_id"))
        associate_id = 1
        cursor = connection.cursor()
        associate_inmate = cursor.execute("SELECT inmate_id from inmate_associates where associate_id = "+associate_id)
        row = cursor.fetchall()
        associate_inmate_list= []
        for i in row:
            associate_inmate_list.append(i)
        print associate_inmate_list
        return render_to_response("associate_inmate.html", {'associate_inmate_list': associate_inmate_list}, context_instance=RequestContext(request))

def associate_schedule(request):
    if request.method == 'POST':
        cursor = connection.cursor()
        inmate_id = str(request.POST.get("inmate_id"))
        associate_id = str(request.POST.get("associate_id"))
        visit_start_time = str(request.POST.get("visit_start_time"))
        visit_end_time = str(request.POST.get("visit_end_time"))
        visit_type = str(request.POST.get("visit_type"))
        associate_schedule = cursor.execute(
            "INSERT INTO inmate_associates_visits(inmate_id, associate_id, visit_start_time, visit_end_time, visit_type) "
            "VALUES ("+inmate_id+","+associate_id+","+visit_start_time+","+visit_end_time+","+visit_type+")")
        return render_to_response("associate_schedule.html",{},
                                  context_instance=RequestContext(request))

    if request.method == 'GET':
        cursor = connection.cursor()
        associate_schedule = cursor.execute(
            "SELECT inmate_id, associate_id, visit_start_time, visit_end_time, visit_type from inmate_associates_visits where associate_id = " + associate_id + ")")
        row = cursor.fetchall()
        associate_schedule_list = []
        for i in row:
            associate_schedule_list.append(i)
        print associate_schedule_list
        return render_to_response("associate_schedule.html", {'associate_schedule_list': associate_inmate_list},
                                  context_instance=RequestContext(request))

def warden_approved(request):
    if request.method == 'POST':
        cursor = connection.cursor()
        warden_approved = cursor.execute("INSERT INTO inmate_warden()")


