from django.urls import path
from django.contrib.auth.views import (LoginView, LogoutView)

from users.views import (SignupAPIView, ChangeAvatarAPIView, SignupView)
from users.forms import CaptchaLoginForm

from rest_framework.authtoken.views import (obtain_auth_token,)

app_name = 'users'

urlpatterns = [
    path('api/signup/', SignupAPIView.as_view(), name='signup_api_view'),
    path('api/login/', obtain_auth_token, name='login_api_view'),
    path('api/avatar/', ChangeAvatarAPIView.as_view(), name='change_avatar_api_view'),
    path('signup/', SignupView.as_view(), name='signup_view'),
    path('login/', LoginView.as_view(template_name='users/login_view.html', form_class=CaptchaLoginForm), name='login_view'),
    path('logout/', LogoutView.as_view(template_name='users/logout_view.html'), name='logout_view'),
]