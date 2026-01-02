from sys import flags
from django_filters.rest_framework import DjangoFilterBackend
from django.contrib.auth.models import User
from rest_framework import filters, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import (
    ExtensionSerializer,
    ModerationFlagSerializer,
    ReviewSerializer,
)
from .moderation import run_moderation_checks

from .models import Extension, ModerationFlag, Review
from extensions import serializers


class ExtensionViewSet(viewsets.ModelViewSet):
    """
    ViewSet for Extension CRUD operations.
    Provides: list, create, retrieve, update, destroy
    """

    queryset = Extension.objects.all()
    serializer_class = ExtensionSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ["status", "developer"]
    search_fields = ["name", "description"]
    ordering_fields = ["created_at", "downloads"]

    @action(detail=False, methods=["get"])
    def pending(self, request):
        """Custom endpoint: /api/extensions/pending/ - for reviewer queue"""
        pending_extensions = self.queryset.filter(status="pending")
        serializer = self.get_serializer(pending_extensions, many=True)
        return Response(serializer.data)

    def perform_create(self, serializer):
        """Overide to add a developer and run automated checks"""
        developer = self.request.user if self.request.user.is_authenticated else User.objects.first()
        extension = serializer.save(developer=developer)
        flags = run_moderation_checks(extension)
        for flag in flags:
            flag.save()

        if any(flag.severity == "critical" for flag in flags):
            extension.status = "rejected"
            extension.save()
        elif any(flag.severity == "warning" for flag in flags):
            extension.status = "flagged"
            extension.save()


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["extension", "reviewer", "decision"]


class ModerationFlagViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Read-only viewset for moderation flags.
    These are created by automated systems, not manually.
    """

    queryset = ModerationFlag.objects.all()
    serializer_class = ModerationFlagSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["extension", "severity"]
