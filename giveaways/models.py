from django.conf import settings
from django.db import models
from django.utils import timezone

class GiveawayItem(models.Model):
    CATEGORIES = [
        ("Books", "Books"),
        ("Electronics", "Electronics"),
        ("Clothing", "Clothing"),
        ("Home", "Home & Kitchen"),
        ("Stationery", "Stationery"),
        ("Other", "Other"),
    ]
    STATUS_CHOICES = [
        ("available", "Available"),
        ("claimed", "Claimed"),
    ]

    title = models.CharField(max_length=100)
    description = models.TextField(max_length=800)
    category = models.CharField(max_length=20, choices=CATEGORIES, default="Other")
    location = models.CharField(max_length=120)
    contact_info = models.CharField(max_length=120, help_text="Email or preferred contact method")
    collection_deadline = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=12, choices=STATUS_CHOICES, default="available")
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="giveaway_items")
    claimed_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name="claimed_items")
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ["-created_at"]

    @property
    def is_expired(self):
        return bool(self.collection_deadline and self.collection_deadline < timezone.localdate() and self.status == "available")

    def __str__(self):
        return self.title
