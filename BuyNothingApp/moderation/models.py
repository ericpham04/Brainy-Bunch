from django.db import models
from django.contrib.auth.models import User
from listings.models import Listing


class Report(models.Model):
    reporter = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reports")
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="reports")
    reason = models.TextField()
    reviewed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Report on {self.listing.title}"