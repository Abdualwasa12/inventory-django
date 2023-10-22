from django.shortcuts import redirect, render
from .models import Employee
from .forms import EmployeeForm ,SignupForm
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from .forms import LoginForm
from django.contrib.auth.decorators import login_required,permission_required



# Create your views here.
@login_required
@permission_required('accounts.view_employee')
def adminer_list(request):
    adminers = Employee.objects.all()
    return render (request, 'adminer_list.html',{'adminers':adminers})





def signin(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('inventory:home')
        form = LoginForm()
        return render(request,'registration/login.html', {'form': form})
    
    elif request.method == 'POST':
        form = LoginForm(request.POST)
        
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request,username=username,password=password)
            if user:
                login(request, user)
                messages.success(request,f'مرحبا {username.title()},عوداً حميداً')
                return redirect('inventory:home')
        
        # form is not valid or user is not authenticated
        messages.error(request,f'خطأ في اسم المستخدم او كلمة المرور')
        return render(request,'registration/login.html',{'form': form})

def signup(request):
    if request.method=="POST":
        signup_form = SignupForm(request.POST)
        employee_form = EmployeeForm(request.POST)

        if signup_form.is_valid() and employee_form.is_valid():
             # Create the user
            user = signup_form.save()
             # Check if an employee instance already exists for the user
            employee, created = Employee.objects.get_or_create(user=user)

            if not created:
                # employee instance already exists, update the name and phone fields
                employee.name = employee_form.cleaned_data['name']
                employee.phone = employee_form.cleaned_data['phone']
                employee.save()

            # Log the user in
            username = signup_form.cleaned_data['username']
            password = signup_form.cleaned_data['password1']
            
            user = authenticate(username=username,password=password)
            login(request,user)
            messages.success(request,f'مرحبا {username.title()}, تم تسجيل الدخول بنجاح')
            return redirect('inventory:home')
    else:
        signup_form = SignupForm()
        employee_form = EmployeeForm()
    return render(request,'registration/signup.html',{'signup_form': signup_form, 'employee_form': employee_form})

def signout(request):
    logout(request)
    messages.success(request,f'لقد تم تسجيل الخروج.')
    return redirect('accounts:signin')    





