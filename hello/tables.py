import django_tables2 as tables
from .models import Shop, Provider

class ShopTable(tables.Table):
    class Meta:
        model = Shop
        # add class="paleblue" to <table> tag
        attrs = {'class': 'paleblue'}
        fields = ("number", "address","filial.name", "provider.name", "provider.contract", "provider.entity", "provider.tel_number", "speed", "tel_number", "kass_count", "license_astor.TS", "license_astor.SIS", "license_astor.MDT", "license_astor.LP" )