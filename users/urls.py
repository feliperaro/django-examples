from django.urls import path

from users.views import (SignupAPIView,)
from rest_framework.authtoken.views import (obtain_auth_token,)

app_name = 'users'

urlpatterns = [
    path('api/signup/', SignupAPIView.as_view(), name='signup_api_view'),
    path('api/login/', obtain_auth_token, name='login_api_view')
]