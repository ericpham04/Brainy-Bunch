from django.shortcuts import render

from .models import Listing


def browse_listings(request):
    """
    Display community listings that are currently available.

    Pending and completed/gone listings are deliberately excluded.
    The secondary ordering by primary key makes the ordering
    deterministic when two records have the same creation time.
    """
    available_listings = (
        Listing.objects
        .filter(status="available")
        .select_related("owner")
        .order_by("-created_at", "-pk")
    )

    return render(
        request,
        "listings/browse.html",
        {"listings": available_listings},
    )
