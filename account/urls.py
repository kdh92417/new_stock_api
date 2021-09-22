from django.urls    import path
from account.views  import (
    SignupView,
    SigninView,
    RegisterView
)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('sign-up/', RegisterView.as_view()),
    path('sign-in/', TokenObtainPairView.as_view(), name='sign-in'),
]