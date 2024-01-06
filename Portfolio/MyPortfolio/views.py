from django.shortcuts import render
from .models import RobotsTxt

# Create your views here.

def keytalk(request) :
    data = RobotsTxt.objects.all()

    return render(request, "main.html", {"data" : data})