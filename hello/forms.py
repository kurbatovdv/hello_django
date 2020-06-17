from django import forms
from .models import Shop, Cartridge_journal


class ShopForm(forms.ModelForm):

    class Meta:
        model = Shop
        fields = ('number', 'address', 'filial', 'provider', 'speed',
                  'tel_number', 'kass_count', 'license_astor')


class CartridgeForm(forms.ModelForm):

    class Meta:
        model = Cartridge_journal
        fields = ('cartridge', 'department')
