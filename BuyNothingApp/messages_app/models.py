from django.conf import settings
from django.db import models
from listings.models import Listing

class Message(models.Model):
    listing=models.ForeignKey(Listing,on_delete=models.CASCADE,related_name="messages",null=True,blank=True)
    sender=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name="sent_messages")
    receiver=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name="received_messages")
    text=models.TextField()
    is_read=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    class Meta: ordering=["created_at"]
    def __str__(self): return f"Message from {self.sender} to {self.receiver}"
