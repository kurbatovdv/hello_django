import django_tables2 as tables
from .models import Shop, Provider, Cartridge_journal


class ShopTable(tables.Table):
    class Meta:
        model = Shop
        # add class="paleblue" to <table> tag
        attrs = {'class': 'paleblue'}
        fields = ("number", "address", "time_open", "time_close", "filial.name", "provider.name", "provider.contract", "provider.entity",
                  "provider.tel_number", "speed", "tel_number", "kass_count", "license_astor.TS", "license_astor.SIS", "license_astor.MDT", "license_astor.LP")


class CartridgeTable(tables.Table):
    class Meta:
        model = Cartridge_journal
        # add class="paleblue" to <table> tag
        attrs = {'class': 'paleblue'}
        fields = ("cartridge", "department", "time")


class CartridgeRegistrationTable(tables.Table):
    class Meta:
        model = Cartridge_journal
        # add class="paleblue" to <table> tag
        attrs = {'class': 'paleblue'}
        fields = ("cartridge", "department", "time", "created_count")
