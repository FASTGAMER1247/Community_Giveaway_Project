from django.contrib import admin
from .models import GiveawayItem

@admin.register(GiveawayItem)
class GiveawayItemAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "location", "status", "created_by", "created_at", "collection_deadline")
    list_filter = ("status", "category", "created_at")
    search_fields = ("title", "description", "location", "created_by__username")
