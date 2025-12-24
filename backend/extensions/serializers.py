from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Extension, ModerationFlag, Review


class UserSerializer(serializers.ModelSerializer):
    """Seriliazer for User model -- only expose safe fields"""

    class Meta:
        model = User
        fields = ["id", "username", "email"]


class ModerationFlagSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModerationFlag
        fields = "__all__"


class ReviewSerializer(serializers.ModelSerializer):
    reviewer = UserSerializer(read_only=True)

    class Meta:
        model = Review
        fields = "__all__"


class ExtensionSerializer(serializers.ModelSerializer):
    developer = UserSerializer(read_only=True)
    reviews = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = Extension
        fields = "__all__"
        read_only_fields = ["downloads", "created_at", "updated_at"]
