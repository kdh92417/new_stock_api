from django.urls import path
from account.views import (
    RegisterView,
    ChangeUserInfoView
)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('sign-up/', RegisterView.as_view()),
    path('sign-in/', TokenObtainPairView.as_view(), name='sign-in'),
    path('update/<int:pk>/', ChangeUserInfoView.as_view())
]
