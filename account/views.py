from rest_framework.views            import APIView
from rest_framework.response         import Response
from rest_framework.authtoken.models import Token

from django.contrib.auth             import authenticate
from django.contrib.auth.models      import User

from account.models                  import Account


class SignupView(APIView):
    def post(self, request):
        user = User.objects.create_user(
                username=request.data['username'], 
                password=request.data['password'],
                email=request.data['email']
            )
        account = Account(
                    user=user, 
                    birth_date=request.data['birth_date'],
                    phone_number=request.data['phone_number']
                )

        user.save()
        account.save()

        token = Token.objects.create(user=user)
        return Response({"Token": token.key})
    

class LoginView(APIView):
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
