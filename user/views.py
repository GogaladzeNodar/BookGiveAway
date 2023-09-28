from django.shortcuts import render
from rest_framework.views import APIView


from django.contrib.auth import authenticate, login, logout
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from .serializers import UserRegistrationSerializer, UserLoginSerializer

class UserRegistratinView(generics.CreateAPIView):
    serializer_class = UserRegistrationSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            {"message": "User registered successfully"},
            status=status.HTTP_201_CREATED,
        )


class UserLoginView(APIView):
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        email = serializer.validated_data['email']
        password = serializer.validated_data['password']

        user = authenticate(email=email, password=password)

        if user is None:
            return Response(data={"error": "Invalid Authentication"}, status=status.HTTP_400_BAD_REQUEST)
        
        login(request, user)

        return Response(status=status.HTTP_200_OK)


class UserLogoutView(APIView):
    def get(self, request):
         logout(request)

         return(Response(status=status.HTTP_200_OK))