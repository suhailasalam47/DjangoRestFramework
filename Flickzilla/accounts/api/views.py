from rest_framework.response import Response
from .serializers import RegistrationSerializer
from rest_framework.decorators import api_view


@api_view(['POST'],)
def register(request):
    serializer = RegistrationSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)