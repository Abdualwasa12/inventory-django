from django.shortcuts import redirect, render,get_object_or_404
from .models import Product
from .forms import ProductForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required,permission_required


# Create your views here.

def home(request):
    return render(request, 'home.html')

@login_required
@permission_required('inventory.view_product')
def prodcut_list(request):
    products = Product.objects.filter(is_deleted=False)
    return render (request, 'product_list.html',{'products':products})

@login_required
@permission_required('inventory.add_product')
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.employee =request.user.employee
            product.save()
            
            messages.success(request,'تم اضافة المنتج بنجاح')
            return redirect('inventory:product_list')
    else:
        form = ProductForm
    return render(request , 'add_product.html', {'form':form})


@login_required
@permission_required('inventory.change_product')
def edit_product(request, id ):
    product =get_object_or_404(Product, id=id)
    if request.method == 'POST':
        form = ProductForm(request.POST,  instance=product) 
        if form.is_valid(): 
            form.save() 
        messages.success(request,'تم تعديل المنتج بنجاح')
        return redirect('inventory:product_list')
    else: 
        form = ProductForm(instance=product) 
        
    return render(request, 'edit_product.html', {'form': form}) 


@login_required
@permission_required('inventory.delete_product')
def delete_product(request, id ):
    product =get_object_or_404(Product, id=id)
    if request.method == 'POST':
        product.is_deleted =True
        product.save() 
        messages.success(request,'تم حذف المنتج بنجاح')
        return redirect('inventory:product_list')
    return render(request, 'delete_product.html')