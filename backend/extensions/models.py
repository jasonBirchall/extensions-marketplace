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
    downloads = models.PositiveIntegerField()

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

class Review(models.Model):
    """
    Represents a reviewer's feedback on an extension submission
    """

    DECISION_CHOICES = [
        ("approved", "Approved"),
        ("rejected", "Rejected"),
        ("needs_changes", "Needs Changes"),
    ]
    
    extension = models.ForeignKey(Extension, on_delete=models.CASCADE, related_name="reviews")
    reviewer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reviews_given")

    decision = models.CharField(max_length=20, choices=DECISION_CHOICES)
    comments = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"Review of {self.extension.name} by {self.reviewer.name}"

class ModerationFlag(models.Model):
    """
    Represents autoamted moderation check results.
    This is the 'automated moderation pipeline' part of the job description!
    """

    SEVERITY_CHOICES = [
        ("info", "Info"),
        ("warning", "Warning"),
        ("critical", "Critical"),
    ]

    extension = models.ForeignKey(Extension, on_delete=models.CASCADE, related_name="flags")

    check_name = models.CharField(max_length=100)
    severity = models.CharField(max_length=10, choices=SEVERITY_CHOICES)
    message = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.severity}: {self.check_name} on {self.extension.name}"

