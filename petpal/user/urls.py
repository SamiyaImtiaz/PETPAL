from django.urls import path
from . import views

urlpatterns = [
    # User URLs
    path('api/users/', views.user_list, name='user_list'),
    path('api/users/<str:user_id>/', views.user_detail, name='user_detail'),

    # Appointment URLs
    path('api/appointments/', views.appointment_list, name='appointment_list'),
    path('api/appointments/<str:appointment_id>/', views.appointment_detail, name='appointment_detail'),
]
