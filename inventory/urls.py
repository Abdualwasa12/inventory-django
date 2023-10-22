from django.urls import path
from . import views
from . import api as api_views 

app_name='inventory'

urlpatterns = [
    path('',views.home, name='home'),
    path('product_list/',views.prodcut_list, name='product_list'),
    path('add_product/',views.add_product, name='add_product'),
    path('edit_product/<int:id>',views.edit_product, name='edit_product'),
    path('delete_product/<int:id>',views.delete_product, name='delete_product'),
    
    # Api
    path('api/', api_views.ProductList.as_view(), name='product-list'),
    path('api/<int:pk>/',api_views.ProductDetail.as_view(), name='product-detail'),

]