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