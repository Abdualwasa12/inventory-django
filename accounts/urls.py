from django.urls import path
from . import views

app_name='adminer'

urlpatterns = [
    path('adminer_list/',views.adminer_list, name='adminer_list'),
    path('signup/',views.signup , name='signup'),
    path('signin/',views.signin , name='signin'),
    path('signout/',views.signout , name='signout'),

]