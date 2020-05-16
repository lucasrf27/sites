from django import forms
from .models import Product_sell_create

class ProductName(forms.ModelForm):
    class Meta:
        model = Product_sell_create
        fields = [
            'product_product_sell',
            'product_volume_sell',
            'product_price_sell',
            'product_location_sell',
            'product_description_sell'
        ]