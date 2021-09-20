from django.urls    import path, include
from account.views  import (
    SignupView,
    LoginView    
)

urlpatterns = [
    path('sign-up/', SignupView.as_view()),
    path('sign-in/', LoginView.as_view()),
]
