from rest_framework import serializers
from .models import User, Appointment

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['user_id', 'user_type', 'name', 'email', 'password', 'contact', 'address']

class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = ['appointment_id', 'date', 'user', 'vet']
