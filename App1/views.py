from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.
def display(request):
    return HttpResponse("<h1>hola mundo!</h1>")

def displayDatetime(request):
    dt = datetime.datetime.now()
    s = "<b> Fecha y hora Actual: </b>" + str(dt)
    return HttpResponse(s)