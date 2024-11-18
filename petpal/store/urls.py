from django.urls import path
from . import views

urlpatterns = [
    # Store CRUD URLs
    path('api/stores/', views.store_list, name='store_list'),
    path('api/stores/<str:store_id>/', views.store_detail, name='store_detail'),

    # Product CRUD URLs
    path('api/products/', views.product_list, name='product_list'),
    path('api/products/<str:product_id>/', views.product_detail, name='product_detail'),

    # GroomingService CRUD URLs
    path('api/grooming-services/', views.grooming_service_list, name='grooming_service_list'),
    path('api/grooming-services/<str:service_id>/', views.grooming_service_detail, name='grooming_service_detail'),
]
