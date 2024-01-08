from django.shortcuts import render
from .models import RobotsTxt, Folder

# Create your views here.

def robots_txt(request) :
    robots_txt = RobotsTxt.objects.all()

    return render(request, "main.html", {"robots_txt" : robots_txt})


def floder(request) :
    floder = Folder.objects.all()

    return render(request, "main.html", {"floder" : floder})
