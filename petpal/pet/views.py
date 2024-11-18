from rest_framework import viewsets
from .models import Pet
from .serializers import PetSerializer

class PetViewSet(viewsets.ModelViewSet):
    """
    A ViewSet for CRUD operations on the Pet model.
    """
    queryset = Pet.objects.all()
    serializer_class = PetSerializer
