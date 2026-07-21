from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.test import TestCase
from django.urls import reverse
from listings.models import Listing
from .models import ItemRequest

class ItemRequestTests(TestCase):
    def setUp(self):
        self.owner=User.objects.create_user(username="owner",password="pass12345")
        self.requester=User.objects.create_user(username="requester",password="pass12345")
        self.other=User.objects.create_user(username="other",password="pass12345")
        self.listing=Listing.objects.create(owner=self.owner,title="Desk lamp",description="Working desk lamp",category="Home")
    def test_user_can_submit_request(self):
        self.client.login(username="requester",password="pass12345")
        response=self.client.post(reverse("requests_app:request_listing",args=[self.listing.id]),{"message":"I can pick it up today."})
        self.assertRedirects(response,reverse("requests_app:my_requests"))
        self.assertTrue(ItemRequest.objects.filter(listing=self.listing,requester=self.requester).exists())
    def test_duplicate_request_is_prevented(self):
        ItemRequest.objects.create(listing=self.listing,requester=self.requester)
        self.client.login(username="requester",password="pass12345")
        self.client.post(reverse("requests_app:request_listing",args=[self.listing.id]),{"message":"Second request"})
        self.assertEqual(ItemRequest.objects.filter(listing=self.listing,requester=self.requester).count(),1)
    def test_owner_cannot_request_own_listing(self):
        with self.assertRaises(ValidationError):
            ItemRequest(listing=self.listing,requester=self.owner).full_clean()
    def test_listing_owner_can_accept_request(self):
        ir=ItemRequest.objects.create(listing=self.listing,requester=self.requester)
        self.client.login(username="owner",password="pass12345")
        response=self.client.post(reverse("requests_app:update_request_status",args=[ir.id,"accepted"]))
        self.assertRedirects(response,reverse("requests_app:received_requests"))
        ir.refresh_from_db(); self.listing.refresh_from_db()
        self.assertEqual(ir.status,ItemRequest.STATUS_ACCEPTED)
        self.assertEqual(self.listing.status,"pending")
    def test_non_owner_cannot_accept_request(self):
        ir=ItemRequest.objects.create(listing=self.listing,requester=self.requester)
        self.client.login(username="other",password="pass12345")
        response=self.client.post(reverse("requests_app:update_request_status",args=[ir.id,"accepted"]))
        self.assertEqual(response.status_code,403)
