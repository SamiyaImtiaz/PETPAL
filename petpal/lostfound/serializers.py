from rest_framework import serializers
from .models import LostFound

class LostFoundSerializer(serializers.ModelSerializer):
    class Meta:
        model = LostFound
        fields = ['entry_id', 'location', 'details', 'date_reported', 'status']
