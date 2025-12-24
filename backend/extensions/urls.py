from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import ExtensionViewSet, ModerationFlagViewSet, ReviewViewSet

# DRF Router automatically generates URLs for ViewSets
router = DefaultRouter()
router.register(r"extensions", ExtensionViewSet, basename="extension")
router.register(r"reviews", ReviewViewSet, basename="review")
router.register(r"flags", ModerationFlagViewSet, basename="flag")

urlpatterns = [
    path("", include(router.urls)),
]
