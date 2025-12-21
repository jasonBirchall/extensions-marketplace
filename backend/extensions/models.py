from django.contrib.auth.models import User
from django.db import models


class Extension(models.Model):
    """
    Reporesentation of an extension submitted to the marketplace.
    """

    STATUS_CHOICES = [
        ("pending", "Pending Review"),
        ("approved", "Approved"),
        ("rejected", "Rejected"),
        ("flagged", "Flagged for Review"),
    ]

    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)  # URL friendly identifier
    description = models.TextField()
    version = models.CharField(max_length=50)
    developer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="extentions")

    icon = models.ImageField(upload_to="extensions/icons/", null=True, blank=True)
    extension_file = models.FileField(upload_to="extensions/files/")

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="pending")
    downloads = models.PositiveIntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]
        indexes = [
            models.Index(fields=["status", "-created_at"]),
        ]

    def __str__(self):
        """String represenetation of the extension."""
        return f"{self.name} v{self.version}"
