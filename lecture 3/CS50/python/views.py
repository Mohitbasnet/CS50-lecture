from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request, "python/index.html")


def greet(request, name):

    return render(request,"python/greet.html",{
        "name": name.capitalize()
    })