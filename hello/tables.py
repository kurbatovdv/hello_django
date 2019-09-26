import django_tables2 as tables
from .models import Shop

class ShopTable(tables.Table):
    class Meta:
        model = Shop
        # add class="paleblue" to <table> tag
        attrs = {'class': 'paleblue'}