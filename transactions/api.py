from rest_framework import generics
from .models import SaleProduct
from .serializers import SaleProductSerializer

class SaleProductList(generics.ListCreateAPIView):
    queryset = SaleProduct.objects.all()
    serializer_class = SaleProductSerializer

class SaleProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = SaleProduct.objects.all()
    serializer_class = SaleProductSerializer