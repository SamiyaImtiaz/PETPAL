from django.urls import path
from . import views

urlpatterns = [
    # Rehabiliation Center CRUD URLs
    path('api/rehabiliation-centers/', views.rehabiliation_center_list, name='rehabiliation_center_list'),
    path('api/rehabiliation-centers/<str:center_id>/', views.rehabiliation_center_detail, name='rehabiliation_center_detail'),
]
