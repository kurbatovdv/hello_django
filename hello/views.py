import re
from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Replace the existing home function with the one below
@login_required
def home(request):
    return render(request, "hello/home.html")

def about(request):
    return render(request, "hello/about.html")


def contact(request):
    return render(request, "hello/contact.html")

@login_required
def hello_there(request, name):
    return render(
        request,
        'hello/hello_there.html',
        {
            'name': name,
            'date': datetime.now()
        }
    )