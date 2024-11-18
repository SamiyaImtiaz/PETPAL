from django.urls import path
from . import views

urlpatterns = [
    # LostFound CRUD URLs
    path('api/lost-found/', views.lost_found_list, name='lost_found_list'),
    path('api/lost-found/<int:entry_id>/', views.lost_found_detail, name='lost_found_detail'),
]
