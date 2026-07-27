from django.test import TestCase
from django.urls import reverse


class HomePageFrontendTests(TestCase):

    def test_home_page_loads_successfully(self):
        """The home page should return HTTP status 200."""
        response = self.client.get(reverse("home"))

        self.assertEqual(response.status_code, 200)

    def test_home_page_uses_correct_template(self):
        """The home view should render the home.html template."""
        response = self.client.get(reverse("home"))

        self.assertTemplateUsed(response, "home.html")

    def test_home_page_contains_main_content(self):
        """The home page should display important frontend content."""
        response = self.client.get(reverse("home"))

        self.assertContains(response, "Helping Neighbors Help Neighbors")
        self.assertContains(response, "Browse Community Items")
        self.assertContains(response, "Share an Item")

    def test_home_page_contains_navigation(self):
        """The shared navigation bar should appear on the home page."""
        response = self.client.get(reverse("home"))

        self.assertContains(response, "Home")
        self.assertContains(response, "Browse")
        self.assertContains(response, "Share")
        self.assertContains(response, "Notifications")
        self.assertContains(response, "Profile")


class ShareItemPageTests(TestCase):

    def test_share_item_page_loads_successfully(self):
        """The Share an Item page should return HTTP status 200."""
        response = self.client.get(reverse("share"))

        self.assertEqual(response.status_code, 200)

    def test_share_item_page_uses_correct_template(self):
        """The Share an Item page should use create_listing.html."""
        response = self.client.get(reverse("share"))

        self.assertTemplateUsed(response, "create_listing.html")

    def test_share_item_page_contains_form_content(self):
        """The Share an Item page should display the expected form content."""
        response = self.client.get(reverse("share"))

        self.assertContains(response, "Share an Item")
        self.assertContains(response, "Item Name")
        self.assertContains(response, "Category")
        self.assertContains(response, "Condition")
        self.assertContains(response, "Description")
        self.assertContains(response, "Upload Photo")
        self.assertContains(response, "Share Item")

    def test_share_item_page_contains_navigation(self):
        """The Share an Item page should display the navigation menu."""
        response = self.client.get(reverse("share"))

        self.assertContains(response, "Home")
        self.assertContains(response, "Browse")
        self.assertContains(response, "Share")
        self.assertContains(response, "Notifications")
        self.assertContains(response, "Profile")