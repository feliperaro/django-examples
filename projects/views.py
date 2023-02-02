from django.shortcuts import render

from rest_framework.generics import (CreateAPIView, ListAPIView, DestroyAPIView, UpdateAPIView)
from rest_framework.permissions import IsAuthenticated

from projects.serializers import ProjectSerializer
from projects.models import Project

from djangoexamples.permissions import IsOwnerPermission

class ProjectCreateAPIView(CreateAPIView):
    permission_classes = [IsAuthenticated,]
    serializer_class = ProjectSerializer

class ProjectUpdateAPIView(UpdateAPIView):
    permission_classes = [IsAuthenticated, IsOwnerPermission]
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()

class ProjectListAPIView(ListAPIView):
    permission_classes = [IsAuthenticated,]
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()

class ProjectDestroyAPIView(DestroyAPIView):
    permission_classes = [IsAuthenticated, IsOwnerPermission]
    queryset = Project.objects.all()