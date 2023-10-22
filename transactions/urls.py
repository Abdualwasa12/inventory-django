from django.urls import path
from . import views
from . import api as api_views


app_name='transactions'


urlpatterns = [
        path('export_list/',views.export_list, name='export_list'),
        path('new_export/', views.new_export, name='new_export'),
    
        # Api
        path('api/', api_views.SaleProductList.as_view(), name='saleproduct-list'),
        path('api/<int:pk>/',api_views.SaleProductDetail.as_view(), name='saleproduct-detail'),

]