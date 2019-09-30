from django.contrib import admin
from .models import Filial, Provider, Shop, License_Astor

# Register your models here.
admin.site.register(Filial)
admin.site.register(Provider)
admin.site.register(Shop)
admin.site.register(License_Astor)