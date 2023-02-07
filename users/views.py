from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (CreateView,)

from rest_framework.generics import (CreateAPIView,)
from rest_framework.permissions import (AllowAny, IsAuthenticated)

from rest_framework.parsers import (MultiPartParser, FormParser)
from rest_framework.views import APIView
from rest_framework.response import Response

from users.serializers import (SignupSerializer, AvatarSerializer)
from users.forms import SignupForm

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