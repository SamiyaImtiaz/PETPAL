from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import RehabiliationCenter
from .serializers import RehabiliationCenterSerializer

# CRUD operations for RehabiliaionCenter
@api_view(['GET', 'POST'])
def rehabiliation_center_list(request):
    if request.method == 'GET':
        centers = RehabiliationCenter.objects.all()
        serializer = RehabiliationCenterSerializer(centers, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = RehabiliationCenterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def rehabiliation_center_detail(request, center_id):
    try:
        center = RehabiliationCenter.objects.get(center_id=center_id)
    except RehabiliationCenter.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = RehabiliationCenterSerializer(center)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = RehabiliationCenterSerializer(center, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        center.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
