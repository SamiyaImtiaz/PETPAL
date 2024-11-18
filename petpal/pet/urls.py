from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PetViewSet

# Create a router and register the PetViewSet
router = DefaultRouter()
router.register(r'pets', PetViewSet, basename='pet')

urlpatterns = [
    path('', include(router.urls)),
]
