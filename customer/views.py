from django.shortcuts import get_object_or_404, redirect, render
from .models import Customer
from .forms import CustomerForm
from django.contrib.auth.decorators import login_required,permission_required
from django.contrib import messages


# Create your views here.

@login_required
@permission_required('customer.view_customer')
def customer_list(request,):
    customers = Customer.objects.all()
    return render (request, 'customer_list.html',{'customers':customers})



@login_required
@permission_required('customer.add_customer')
def add_customer(request):
    if request.method == 'POST':
       form =CustomerForm(request.POST)
       if form.is_valid():
            form.save()
            messages.success(request,'تم تسجيل العميل بنجاح')
            return redirect('customer:customer_list')
    else:
        form = CustomerForm()
    return render(request,'add_customer.html',{'form':form})


@login_required
@permission_required('customer.change_customer')
def edit_customer(request, id ):
    customer =get_object_or_404(Customer, id=id)
    if request.method == 'POST':
        form = CustomerForm(request.POST,  instance=customer) 
        if form.is_valid(): 
            form.save() 
        messages.success(request,'تم تعديل معلومات العميل بنجاح')
        return redirect('customer:customer_list')
    else: 
        form = CustomerForm(instance=customer) 
        
    return render(request, 'edit_customer.html', {'form': form}) 



@login_required
@permission_required('customer.delete_customer')
def delete_customer(request, id ):
    customer =get_object_or_404(Customer, id=id)
    if request.method == 'POST':
        customer.delete()

        messages.success(request,'تم حذف العميل بنجاح')
        return redirect('customer:customer_list')
    return render(request, 'delete_customer.html')