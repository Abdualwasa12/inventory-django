from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.



class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name =models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
  


    def __str__(self):
        return str(self.name)

## create new user ---> create new empty profile


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Employee.objects.create(user=instance)

    