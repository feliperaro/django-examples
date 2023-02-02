from django.contrib.auth import get_user_model

from projects.models import Project

from rest_framework import serializers

User = get_user_model()

class ProjectSerializer(serializers.ModelSerializer):

    owner = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), required=True)

    class Meta:
        model = Project
        fields = ['id', 'owner', 'name']
        extra_kwargs = {
            'id': {'read_only': True}
        }