from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Note, Profile


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ["firstname", "lastname", "sexe", "dateofbirth", "phonenumber", "email", "role"]


class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()

    class Meta:
        model = User
        fields = ["id", "username", "password", "profile"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        profile_data = validated_data.pop('profile')
        user = User.objects.create_user(username=validated_data['username'], password=validated_data['password'])
        Profile.objects.create(user=user, **profile_data)
        return user