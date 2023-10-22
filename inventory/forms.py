from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
 
    class Meta:
        model = Product
        fields = ['proudct_name', 'proudct_quantity', 'proudct_kind' , 'proudct_num']