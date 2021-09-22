from rest_framework import generics
from rest_framework.views            import APIView
from rest_framework.response         import Response
from rest_framework.permissions      import AllowAny
from rest_framework.authtoken.models import Token

from django.contrib.auth             import authenticate

from account.models                  import User
from account.serializers             import RegisterSerializer


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer
    
    
class SignupView(APIView):
    def post(self, request):
        user = User.objects.create_user(
                username=request.data['username'], 
                password=request.data['password'],
            )
        user.save()

        token = Token.objects.create(user=user)
        return Response({"Token": token.key})
    

class SigninView(APIView):
    def post(self, request):
        user = authenticate(
                    username=request.data['username'], 
                    password=request.data['password']
                )
        
        if user is not None:
            token = Token.objects.get(user=user)
            return Response({"Token": token.key})
        else:
            return Response(status=401)