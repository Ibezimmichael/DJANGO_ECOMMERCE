from django import forms
from .models import ShippingAddress, OrderItem, Order


class ShippingForm(forms.ModelForm):

    class Meta:
        model = ShippingAddress
        fields = ['full_name', 'email', 'address1', 'address2', 'city', 'state']
        exclude = ['user',]