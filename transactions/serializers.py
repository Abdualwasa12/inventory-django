from rest_framework import serializers
from .models import SaleProduct

class SaleProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = SaleProduct
        fields = '__all__'
