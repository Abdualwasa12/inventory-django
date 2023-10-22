from django import forms
from django.forms import formset_factory
from .models import SaleProduct




class SaleProductForm(forms.ModelForm):

    class Meta:
        model = SaleProduct
        fields = ['customer','product', 'quantity']

# formset used to render multiple 'SaleItemForm'
SaleProductFormset = formset_factory(SaleProductForm, extra=1)
