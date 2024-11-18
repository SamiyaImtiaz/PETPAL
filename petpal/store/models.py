from django.db import models
from user.models import User

class Store(models.Model):
    STORE_TYPES = [
        ('product', 'Product'),
        ('service', 'Service'),
    ]

    store_id = models.CharField(max_length=50, primary_key=True)
    store_name = models.CharField(max_length=100)
    location = models.TextField()
    store_type = models.CharField(max_length=20, choices=STORE_TYPES)
    store_owner = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'user_type': 'storeOwner'})

    def __str__(self):
        return self.store_name


class Product(models.Model):
    product_id = models.CharField(max_length=50, primary_key=True)
    product_name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock_status = models.BooleanField()
    store = models.ForeignKey(Store, on_delete=models.CASCADE)

    def __str__(self):
        return self.product_name


class GroomingService(models.Model):
    service_id = models.CharField(max_length=50, primary_key=True)
    service_name = models.CharField(max_length=100)
    pet_type = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.IntegerField()  # Duration in minutes
    store = models.ForeignKey(Store, on_delete=models.CASCADE)

    def __str__(self):
        return self.service_name
