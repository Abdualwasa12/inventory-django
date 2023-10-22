from django.db import models
from accounts.models import Employee
# Create your models here.

class Product(models.Model):
    proudct_num = models.IntegerField()
    proudct_name = models.CharField(max_length=200)
    proudct_quantity = models.PositiveIntegerField()
    proudct_kind = models.CharField(max_length=100)
    
    employee =models.ForeignKey(Employee,on_delete=models.PROTECT)
    is_deleted = models.BooleanField(default=False)
    def __str__(self):
        return self.proudct_name
    
    
    
        