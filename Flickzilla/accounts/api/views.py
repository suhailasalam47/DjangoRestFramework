from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from .serializers import RegistrationSerializer
from rest_framework.decorators import api_view
from accounts import models
from rest_framework import status


@api_view(['POST',])
def logout(request):
    
    if request.method == 'POST':
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)


@api_view(['POST'],)
def register(request):
    serializer = RegistrationSerializer(data=request.data)

    data ={}

    if serializer.is_valid():
        account = serializer.save()

        data['response'] = "Registration Successful"
        data['username'] = account.username
        data['email'] = account.email

        token = Token.objects.get(user=account).key
        data['token'] = token

    else:
        data = serializer.errors

    return Response(data)