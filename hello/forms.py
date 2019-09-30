from django import forms
from .models import Shop

class ShopForm(forms.ModelForm):

    class Meta:
        model = Shop
        fields = ('number', 'address', 'filial', 'provider', 'speed', 'tel_number','kass_count', 'license_astor')
