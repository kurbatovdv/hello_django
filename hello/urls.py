from django.urls import path
from hello import views

urlpatterns = [
    path("", views.home, name="home"),
    path("hello/<name>", views.hello_there, name="hello_there"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("shops/", views.shops, name="shops"),
    path("shops/new", views.shop_new, name="shop_new"),
    path("cartridge/", views.cartridge_jornal, name="cartridge_jornal"),
    path("cartridge/new", views.cartridge_new, name="cartridge_new"),
    path("cartridges/", views.cartridge_registration, name="cartridge_registration"),
]