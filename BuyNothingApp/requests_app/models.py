from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import models
from listings.models import Listing

class ItemRequest(models.Model):
    STATUS_PENDING = "pending"
    STATUS_ACCEPTED = "accepted"
    STATUS_REJECTED = "rejected"
    STATUS_CANCELLED = "cancelled"
    STATUS_CHOICES = [(STATUS_PENDING,"Pending"),(STATUS_ACCEPTED,"Accepted"),(STATUS_REJECTED,"Rejected"),(STATUS_CANCELLED,"Cancelled")]
    listing = models.ForeignKey(Listing,on_delete=models.CASCADE,related_name="item_requests")
    requester = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name="item_requests")
    message = models.TextField(blank=True)
    status = models.CharField(max_length=20,choices=STATUS_CHOICES,default=STATUS_PENDING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ["-created_at"]
        constraints = [models.UniqueConstraint(fields=["listing","requester"],name="unique_request_per_listing_and_user")]
    def clean(self):
        if self.listing_id and self.requester_id and self.listing.owner_id == self.requester_id:
            raise ValidationError("You cannot request your own listing.")
    def __str__(self):
        return f"{self.requester.username} requested {self.listing.title}"
