from django.db import models

class LostFound(models.Model):
    STATUS_CHOICES = [
        ('lost', 'Lost'),
        ('found', 'Found'),
        ('reunited', 'Reunited'),
    ]

    entry_id = models.AutoField(primary_key=True)
    location = models.TextField()
    details = models.TextField()
    date_reported = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)

    def __str__(self):
        return f"{self.status} - {self.location}"
