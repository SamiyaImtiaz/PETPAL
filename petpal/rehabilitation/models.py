from django.db import models

class RehabilitationCenter(models.Model):
    center_id = models.CharField(max_length=50, primary_key=True)
    location = models.TextField()
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
