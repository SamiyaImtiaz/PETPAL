from django.db import models
from user.models import User

class Pet(models.Model):
    pet_id = models.CharField(max_length=50, primary_key=True)
    breed = models.CharField(max_length=100)
    age = models.IntegerField()
    health_status = models.TextField()
    availability_status = models.BooleanField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'user_type': 'regular'})

    def __str__(self):
        return self.breed
