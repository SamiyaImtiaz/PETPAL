from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import LostFound
from .serializers import LostFoundSerializer

# CRUD operations for LostFound
@api_view(['GET', 'POST'])
def lost_found_list(request):
    if request.method == 'GET':
        entries = LostFound.objects.all()
        serializer = LostFoundSerializer(entries, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = LostFoundSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def lost_found_detail(request, entry_id):
    try:
        entry = LostFound.objects.get(entry_id=entry_id)
    except LostFound.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = LostFoundSerializer(entry)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = LostFoundSerializer(entry, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        entry.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
