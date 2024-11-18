from rest_framework import serializers
from .models import RehabiliationCenter

class RehabiliationCenterSerializer(serializers.ModelSerializer):
    class Meta:
        model = RehabiliationCenter
        fields = ['center_id', 'location', 'name']
