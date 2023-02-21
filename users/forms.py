from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from captcha.fields import CaptchaField

User = get_user_model()

class SignupForm(UserCreationForm):

    captcha = CaptchaField()

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2', 'captcha']

class CaptchaLoginForm(AuthenticationForm):

    captcha = CaptchaField()