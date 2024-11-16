from django.db import models

class User(models.Model):
    USER_TYPES = [
        ('regular', 'Regular'),
        ('vet', 'Vet'),
        ('storeOwner', 'StoreOwner'),
        ('seller', 'Seller'),
        ('adopter', 'Adopter'),
    ]

    user_type = models.CharField(max_length=20, choices=USER_TYPES)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    contact = models.BigIntegerField()
    address = models.TextField()

    def __str__(self):
        return self.name


class Appointment(models.Model):
    appointment_id = models.CharField(max_length=50, primary_key=True)
    date = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="appointments", limit_choices_to={'user_type': 'regular'})
    vet = models.ForeignKey(User, on_delete=models.CASCADE, related_name="vet_appointments", limit_choices_to={'user_type': 'vet'})

    def __str__(self):
        return f"{self.user.name} - {self.date}"
