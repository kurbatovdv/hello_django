from django.contrib import admin
from .models import Filial, Provider, Shop, License_Astor, Cartridge, Department, Cartridge_journal

# Register your models here.
admin.site.register(Filial)
admin.site.register(Provider)
admin.site.register(Shop)
admin.site.register(License_Astor)
admin.site.register(Cartridge)
admin.site.register(Department)
admin.site.register(Cartridge_journal)