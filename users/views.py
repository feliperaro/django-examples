from django.shortcuts import render
from django.http import request
from django.urls import reverse_lazy
from django.views.generic import (CreateView,)

from rest_framework.generics import (CreateAPIView,)
from rest_framework.permissions import (AllowAny, IsAuthenticated)

from rest_framework.parsers import (MultiPartParser, FormParser)
from rest_framework.views import APIView
from rest_framework.response import Response

from users.serializers import (SignupSerializer, AvatarSerializer)
from users.forms import SignupForm
from users.models import EmailConfirmationToken
from users.utils import send_confirmation_email

class SignupAPIView(CreateAPIView):
    serializer_class = SignupSerializer
    permission_classes = [AllowAny,]

class ChangeAvatarAPIView(APIView):
    permission_classes = [IsAuthenticated,]
    parser_classes = [FormParser, MultiPartParser]
    
    def post(self, request, format=None):
        user = request.user
        serializer = AvatarSerializer(instance=user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=200)
        else:
            return Response(data=serializer.errors, status=500)

class SignupView(CreateView):

    template_name = 'users/signup_view.html'
    success_url = reverse_lazy('users:login_view')
    form_class = SignupForm

class UserInformationAPIVIew(APIView):

    permission_classes = [IsAuthenticated,]

    def get(self, request):
        user = request.user
        email = user.email
        is_email_confirmed = user.is_email_confirmed
        payload = {'email': email, 'is_email_confirmed': is_email_confirmed}
        return Response(data=payload, status=200)


class SendEmailConfirmationTokenAPIView(APIView):

    permission_classes = [IsAuthenticated,]

    def post(self, request, format=None):
        user = request.user
        token = EmailConfirmationToken.objects.create(user=user)
        send_confirmation_email(email=user.email, token_id=token.pk, user_id=user.pk)
        return Response(data=None, status=201)
    
def confirm_email_view(request):
    token_id = request.GET.get('token_id', None)
    user_id = request.GET.get('user_id', None)
    try:
        token = EmailConfirmationToken.objects.get(pk=token_id)
        user = token.user
        user.is_email_confirmed = True
        user.save()
        data = {'is_email_confirmed': True}
        return render(request, template_name='users/confirm_email_view.html', context=data)
    except EmailConfirmationToken.DoesNotExist:
        data = {'is_email_confirmed': False}
        return render(request, template_name='users/confirm_email_view.html', context=data)