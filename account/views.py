from django.contrib.auth import authenticate

from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework.decorators import permission_classes
from account.models import User
from account.serializers import (
    RegisterSerializer,
    UserSerializer
)


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


class ChangeUserInfoView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

    # @permission_classes([IsAuthenticated])
    # def get(self, request, foramt=None):

    #     print(request.user)
    #     print(request.user.id)
    #     users = User.objects.all()

    #     serializer = UserSerializer(users, many=True)
    #     return Response(serializer.data)

    # def put(self, request, format=None):
    #     snippet = self.get_object(pk)
    #     serializer = SnippetSerializer(snippet, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
