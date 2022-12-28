from django.shortcuts import render
from django.http import HttpResponse

def suresh(repuest):
    return HttpResponse('<h1>this is my first view in app1</h1>')
def naresh(request):
    return HttpResponse('<h1> this is my second view in app2</h1>')
