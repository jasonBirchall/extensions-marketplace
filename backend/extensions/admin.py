from django.contrib import admin

from .models import Extension, ModerationFlag, Review


@admin.register(Extension)
class ExtensionAdmin(admin.ModelAdmin):
    list_display = ["name", "version", "developer", "status", "downloads", "created_at"]
    list_filter = ["status", "created_at"]
    search_fields = ["name", "description", "developer__username"]
    readonly_fields = ["created_at", "updated_at", "downloads"]
    prepopulated_fields = {"slug": ("name",)}  # auto-generate slug from name


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ["extension", "reviewer", "decision", "created_at"]
    list_filter = ["decision", "created_at"]
    search_fields = ["extension__name", "reviewer__username", "comments"]


@admin.register(ModerationFlag)
class ModerationFlagAdmin(admin.ModelAdmin):
    list_display = ["extension", "check_name", "severity", "created_at"]
    list_filter = ["severity", "check_name", "created_at"]
    search_fields = ["extension__name", "message"]
