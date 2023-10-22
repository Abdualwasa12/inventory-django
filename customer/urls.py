from django.urls import path
from . import views
from . import api as api_views


app_name='customer'

urlpatterns = [
    path('',views.customer_list, name='customer_list'),
    path('add_customer/',views.add_customer, name='add_customer'),
    path('edit_customer/<int:id>',views.edit_customer, name='edit_customer'),
    path('delete_customer/<int:id>',views.delete_customer, name='delete_customer'),
    
    # Api
    path('api/', api_views.CustomerList.as_view(), name='customer-list'),
    path('api/<int:pk>/',api_views.CustomerDetail.as_view(), name='customer-detail'),



]