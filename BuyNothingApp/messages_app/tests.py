from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from listings.models import Listing
from .models import Message

class MessageTests(TestCase):
    def setUp(self):
        self.sender=User.objects.create_user(username="sender",password="pass12345")
        self.receiver=User.objects.create_user(username="receiver",password="pass12345")
        self.listing=Listing.objects.create(owner=self.receiver,title="Free chair",description="Wooden chair",category="Furniture")
    def test_logged_in_user_can_send_message(self):
        self.client.login(username="sender",password="pass12345")
        response=self.client.post(reverse("messages_app:conversation_with_listing",args=[self.receiver.id,self.listing.id]),{"text":"Is this still available?"})
        self.assertEqual(response.status_code,302)
        self.assertTrue(Message.objects.filter(sender=self.sender,receiver=self.receiver,listing=self.listing,text="Is this still available?").exists())
    def test_inbox_only_shows_received_messages(self):
        Message.objects.create(sender=self.sender,receiver=self.receiver,listing=self.listing,text="First message")
        Message.objects.create(sender=self.receiver,receiver=self.sender,listing=self.listing,text="Reply message")
        self.client.login(username="receiver",password="pass12345")
        response=self.client.get(reverse("messages_app:inbox"))
        self.assertContains(response,"First message")
        self.assertNotContains(response,"Reply message")
