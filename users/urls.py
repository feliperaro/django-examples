from django.urls import path
from django.contrib.auth.views import (LoginView, LogoutView)

from users.views import (SignupAPIView, ChangeAvatarAPIView, SignupView, 
                         SendEmailConfirmationTokenAPIView, UserInformationAPIVIew,
                         confirm_email_view)
from users.forms import CaptchaLoginForm

from rest_framework.authtoken.views import (obtain_auth_token,)

app_name = 'users'

urlpatterns = [
    path('api/signup/', SignupAPIView.as_view(), name='signup_api_view'),
    path('api/login/', obtain_auth_token, name='login_api_view'),
    path('api/avatar/', ChangeAvatarAPIView.as_view(), name='change_avatar_api_view'),
    path('api/me/', UserInformationAPIVIew.as_view(), name='user_information_api_view'),
    path('api/send-confirmation-email/', SendEmailConfirmationTokenAPIView.as_view(), name='send_email_confirmation_api_view'),
    path('signup/', SignupView.as_view(), name='signup_view'),
    path('login/', LoginView.as_view(template_name='users/login_view.html', form_class=CaptchaLoginForm), name='login_view'),
    path('logout/', LogoutView.as_view(template_name='users/logout_view.html'), name='logout_view'),
    path('confirm-email/', confirm_email_view, name='confirm_email_view')
]