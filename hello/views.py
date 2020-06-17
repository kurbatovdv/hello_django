import re
from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render
from django_tables2 import RequestConfig
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from .models import Shop, Cartridge_journal
from .tables import ShopTable, CartridgeTable, CartridgeRegistrationTable
from .forms import ShopForm, CartridgeForm
from django.db.models import Count, F

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
        request,        'hello/hello_there.html',
        {
            'name': name,
            'date': datetime.now()
        }
    )


def shops(request):
    table = ShopTable(Shop.objects.all())
    RequestConfig(request).configure(table)
    return render(request, "hello/shops.html", {'shops': table})


@login_required
def shop_new(request):
    if request.method == "POST":
        form = ShopForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('shops')
    else:
        form = ShopForm()

    return render(request, 'hello/shop_edit.html', {'form': form})


def cartridge_jornal(request):
    table = CartridgeTable(Cartridge_journal.objects.all())
    RequestConfig(request).configure(table)
    return render(request, "hello/cartridge.html", {'cartridge': table})


@login_required
def cartridge_new(request):
    if request.method == "POST":
        form = CartridgeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cartridge_jornal')
    else:
        form = CartridgeForm()

    return render(request, 'hello/cartridge_edit.html', {'form': form})


def cartridge_registration(request):
    table = CartridgeRegistrationTable(
        Cartridge_journal.objects.all().annotate(created_count=Count('id')))
    RequestConfig(request).configure(table)
    return render(request, "hello/cartridge.html", {'cartridge': table})
