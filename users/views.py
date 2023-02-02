from django.shortcuts import render

from rest_framework.generics import (CreateAPIView,)
from rest_framework.permissions import (AllowAny,)

from users.serializers import (SignupSerializer,)

class SignupAPIView(CreateAPIView):
    serializer_class = SignupSerializer
    permission_classes = [AllowAny,]