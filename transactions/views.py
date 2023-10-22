from django.shortcuts import render, HttpResponse, redirect
from . import models
from django.contrib.auth.decorators import login_required,permission_required
from django.contrib import messages
from inventory.models import Product
from .models import SaleProduct
from .forms import SaleProductForm
# sell_available_products


@login_required
@permission_required('transactions.view_saleproduct')
def export_list(request):
    products =SaleProduct.objects.all()
    return render (request, 'export_list.html',{'products':products})


@login_required
@permission_required('transactions.add_saleproduct')
def new_export(request):
    if request.method == 'POST':
       form =SaleProductForm(request.POST)
       if form.is_valid():
            product =form.save(commit=False)
            product.employee =request.user.employee
            product.save()
            
            messages.success(request,'تم تصدير المنتج بنجاح')
            return redirect('transactions:export_list')
    else:
        form = SaleProductForm()
    return render(request,'new_export.html',{'form':form})

