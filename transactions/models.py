from django.db import models
from inventory.models import Product
from customer.models import Customer
from accounts.models import Employee

class SaleProduct(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
    product = models.ForeignKey(Product,on_delete=models.PROTECT)
    quantity = models.IntegerField()
    date = models.DateField(auto_now=True)
    employee =models.ForeignKey(Employee,on_delete=models.PROTECT)
    
    def save(self, *args, **kwargs):
        # Decrease the product quantity when a sale is made
        if self.product and self.quantity > 0:
            self.product.proudct_quantity -= self.quantity
            self.product.save()
        super(SaleProduct, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.product)