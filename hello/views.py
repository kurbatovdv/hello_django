import re
from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render
from django_tables2 import RequestConfig
from django.contrib.auth.decorators import login_required
from .models import Shop
from .tables import ShopTable

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

def shops(request):
    table = ShopTable(Shop.objects.all())
    RequestConfig(request).configure(table)
    return render(request, "hello/shops.html", {'shops': table})