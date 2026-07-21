from django.urls import path

from . import views

app_name = "requests_app"

urlpatterns = [
    path(
        "listing/<int:listing_id>/request/",
        views.request_listing,
        name="request_listing",
    ),
    path(
        "my-requests/",
        views.my_requests,
        name="my_requests",
    ),
    path(
        "received-requests/",
        views.received_requests,
        name="received_requests",
    ),
    path(
        "request/<int:request_id>/status/<str:status>/",
        views.update_request_status,
        name="update_request_status",
    ),
    path(
        "request/<int:request_id>/cancel/",
        views.cancel_request,
        name="cancel_request",
    ),
]