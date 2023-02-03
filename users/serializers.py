from django.contrib.auth import get_user_model

from rest_framework import serializers

User = get_user_model()

class SignupSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['email', 'password', 'id']
        extra_kwargs = {
            'password': {'write_only': True},
            'id': {'read_only': True}
        }
    

    def create(self, validated_data):
        user = User.objects.create_user(email=validated_data['email'], password=validated_data['password'])
        return user

class AvatarSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['avatar']

    def update(self, instance, validated_data):
        instance.avatar = validated_data.get('avatar', instance.avatar)
        instance.save()
        return instance