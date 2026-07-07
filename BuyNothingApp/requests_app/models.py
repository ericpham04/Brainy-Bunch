from django.db import models
from django.contrib.auth.models import User
from listings.models import Listing


class ItemRequest(models.Model):
    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("accepted", "Accepted"),
        ("rejected", "Rejected"),
    ]

    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="item_requests")
    requester = models.ForeignKey(User, on_delete=models.CASCADE, related_name="item_requests")
    message = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="pending")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.requester.username} requested {self.listing.title}"