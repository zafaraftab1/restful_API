from rest_framework import serializers
from .import models
from .models import ProfileFeedItem


class HelloSerializer(serializers.Serializer):
    """Serializes a name field for testing our APIView"""
    name = serializers.CharField(max_length=15)


class UserProfileSerializer(serializers.ModelSerializer):
    """Serializer for user profile objects"""
    class Meta:
        model = models.UserProfile
        fields = ('id', 'email', 'name', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        """Create and return a new `UserProfile` instance."""
        user = models.UserProfile.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
        )

        user.set_password(validated_data['password'])
        user.save()
        return user

class ProfileFeedSerializer(serializers.ModelSerializer):
    """Serializer for profile feed objects"""

    class Meta:
        model = models.ProfileFeedItem
        fields = ('id', 'user_profile', 'status_text', 'created_on')
        extra_kwargs = {'user_profile': {'read_only': True}}