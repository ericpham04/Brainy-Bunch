from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Listing


class BrowseListingsBackendTests(TestCase):
    """Tests for the Browse Community Items backend."""

    @classmethod
    def setUpTestData(cls):
        user_model = get_user_model()

        cls.owner = user_model.objects.create_user(
            username="listing_owner",
            password="test-password-123",
        )

        cls.available_listing = Listing.objects.create(
            owner=cls.owner,
            title="Available Desk Lamp",
            description="A working lamp available for pickup.",
            category="Home",
            status="available",
        )

        cls.pending_listing = Listing.objects.create(
            owner=cls.owner,
            title="Pending Bicycle",
            description="A bicycle with a request already in progress.",
            category="Sports",
            status="pending",
        )

        cls.gone_listing = Listing.objects.create(
            owner=cls.owner,
            title="Gone Bookshelf",
            description="This bookshelf has already been collected.",
            category="Furniture",
            status="gone",
        )

        cls.url = reverse("listings:browse")

    def test_browse_page_loads_successfully(self):
        """The Browse endpoint should return HTTP 200."""

        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 200)

    def test_browse_page_uses_correct_template(self):
        """The Browse endpoint should use its Browse template."""

        response = self.client.get(self.url)

        self.assertTemplateUsed(response, "listings/browse.html")

    def test_browse_context_contains_only_available_listings(self):
        """
        The backend should place only available listings in
        the template context.
        """

        response = self.client.get(self.url)

        returned_listings = list(response.context["listings"])

        self.assertEqual(
            returned_listings,
            [self.available_listing],
        )

    def test_browse_page_displays_available_listing(self):
        """Available listing information should appear on the page."""

        response = self.client.get(self.url)

        self.assertContains(
            response,
            self.available_listing.title,
        )
        self.assertContains(
            response,
            self.available_listing.category,
        )
        self.assertContains(
            response,
            self.available_listing.description,
        )
        self.assertContains(
            response,
            self.owner.username,
        )

    def test_browse_page_hides_unavailable_listings(self):
        """Pending and gone listings should not be rendered."""

        response = self.client.get(self.url)

        self.assertNotContains(
            response,
            self.pending_listing.title,
        )
        self.assertNotContains(
            response,
            self.gone_listing.title,
        )