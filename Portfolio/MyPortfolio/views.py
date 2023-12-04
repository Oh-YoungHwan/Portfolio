from django.shortcuts import render
from .models import admin_post

# Create your views here.

def test(request) :
    tests = admin_post

    return render(request, "templates/test.html", {"tests":tests})