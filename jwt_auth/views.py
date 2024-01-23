from rest_framework import status, permissions
from .serializers import RegisterSerializer
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import APIView 
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework.authtoken.serializers import AuthTokenSerializer
from .tokens import create_jwt_token





###############
######## REGISTER USERS:
###############

class RegisterView(APIView):
    serializer_class = RegisterSerializer

    def post(self, request: Request):
        data = request.data

        serializer = self.serializer_class(data=data)

        if serializer.is_valid():
            user = serializer.save()


            response = {
                "MESSAGE": "User Created Successfully", 
                "REGISTERED_USER": serializer.data,
            }

            return Response(data=response, status=status.HTTP_201_CREATED)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):

    def post(self, request: Request):

        username = request.data.get("username")
        password = request.data.get("password")
        
        user = authenticate(username = username, password = password)

        if user is not None:
            token = create_jwt_token(user)
            response = {
                "MESSAGE": "Login Successfull", 
                "TOKEN": token
            }
            return Response(data=response, status=status.HTTP_200_OK)

        else:
            return Response(data={"message": "Invalid email or password"})

