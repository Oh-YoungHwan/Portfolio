from django.shortcuts import render
from .models import admin_post

# Create your views here.

def test(request) :
    tests = admin_post.objects.all

    return render(request, "test.html", {"tests":tests})