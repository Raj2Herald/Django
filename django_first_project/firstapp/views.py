from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template,Context
from .models import Flight

# Create your views here.
def view_hello_world(request):
    return HttpResponse("Hello World")


def view_hello_world_template(request):
    string = "Ram"
    list_of_names= ["Ram","Shyam","Hari"]
    t =  Template("<html><body>Hello world again, {{name}} <br> {% for name in names  %} <h1>{{name }}</h1> {% endfor %} <body></html>")
    context = {
        'name':string,
        'names':list_of_names
    }
    html = t.render(Context(context))
    return HttpResponse(html)

def view_hello_world_test(request):
    return render(request,'flight/test.html')


def view_flights_page(request):
    return render(request,'flight/flights.html')

def view_flight_lists(request):
    list_of_flights= Flight.objects.all()
    print(list_of_flights)
    context_variable = {
        'flights':list_of_flights
    }
    return render(request,'flight/flights.html',context_variable)

def view_fight_form(request):
    return render(request,'flight/flightform.html')

def view_flightdata_save(request):
    if request.method == "POST":
        get_all = request.POST
        get_origin = request.POST['flight_origin']
        print(type(get_origin))
        get_destination = request.POST['flight_destination']
        get_duration = request.POST['flight_duration']
        print(get_origin)
        flight_obj = Flight(origin=get_origin,destination=get_destination,duration=get_duration)
        flight_obj.save()
        return HttpResponse("Record Saved")
    else:
        return HttpResponse("Error record saving")

def view_flightdata_updateform(request,ID):
    print(ID)
    flight_obj = Flight.objects.get(id=ID)
    print(flight_obj)
    context_varible = {
        'flight':flight_obj
    }
    return render(request,'flight/flightupdateform.html',context_varible)

def view_update_form_data_in_db(request,ID):
    flight_obj = Flight.objects.get(id=ID)
    print(flight_obj)
    fligh_form_data = request.POST
    print(fligh_form_data)
    flight_obj.origin = request.POST['flight_origin']
    flight_obj.destination =request.POST['flight_destination']
    flight_obj.duration = request.POST['flight_duration']
    flight_obj.save()

    return HttpResponse("Record Updated!!")
