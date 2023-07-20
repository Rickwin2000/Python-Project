from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import ApiTable
from .serializers import ApiTableSerializer
from rest_framework import status

@api_view(['GET'])
def api(request):
    queryset = ApiTable.objects.all()
    serializer = ApiTableSerializer(queryset, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def post(request):
    serializer = ApiTableSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def put(request,id):
    try:
        instance = ApiTable.objects.get(id=id)
    except ApiTable.DoesNotExist:
        return Response({"error": "Resource not found."}, status=status.HTTP_404_NOT_FOUND)

    serializer = ApiTableSerializer(instance, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
