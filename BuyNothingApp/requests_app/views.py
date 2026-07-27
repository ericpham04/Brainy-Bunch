from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.db import IntegrityError, transaction
from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404, redirect, render
from listings.models import Listing
from .forms import ItemRequestForm
from .models import ItemRequest

@login_required
def request_listing(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)
    if listing.owner_id == request.user.id:
        messages.error(request, "You cannot request your own listing.")
        return redirect("requests_app:my_requests")
    if listing.status != "available":
        messages.error(request, "This listing is not currently available.")
        return redirect("requests_app:my_requests")
    if request.method == "POST":
        form = ItemRequestForm(request.POST)
        if form.is_valid():
            item_request = form.save(commit=False)
            item_request.listing = listing
            item_request.requester = request.user
            try:
                item_request.full_clean()
                with transaction.atomic(): item_request.save()
            except (ValidationError, IntegrityError):
                messages.error(request, "You have already requested this listing.")
            else:
                messages.success(request, "Your request was submitted.")
                return redirect("requests_app:my_requests")
    else:
        form = ItemRequestForm()
    return render(request,"requests_app/request_listing.html",{"form":form,"listing":listing})

@login_required
def my_requests(request):
    qs = ItemRequest.objects.filter(requester=request.user).select_related("listing","listing__owner")
    return render(request,"requests_app/my_requests.html",{"requests_made":qs})

@login_required
def received_requests(request):
    qs = ItemRequest.objects.filter(listing__owner=request.user).select_related("listing","requester")
    return render(request,"requests_app/received_requests.html",{"incoming_requests":qs})

@login_required
def update_request_status(request, request_id, status):
    item_request = get_object_or_404(ItemRequest.objects.select_related("listing"),pk=request_id)
    if item_request.listing.owner_id != request.user.id:
        return HttpResponseForbidden("You do not own this listing.")
    allowed={ItemRequest.STATUS_ACCEPTED,ItemRequest.STATUS_REJECTED}
    if request.method != "POST" or status not in allowed:
        messages.error(request,"Invalid request status update.")
        return redirect("requests_app:received_requests")
    with transaction.atomic():
        item_request.status=status
        item_request.save(update_fields=["status","updated_at"])
        if status==ItemRequest.STATUS_ACCEPTED:
            item_request.listing.status="pending"
            item_request.listing.save(update_fields=["status","updated_at"])
            ItemRequest.objects.filter(listing=item_request.listing,status=ItemRequest.STATUS_PENDING).exclude(pk=item_request.pk).update(status=ItemRequest.STATUS_REJECTED)
    messages.success(request,f"Request marked as {status}.")
    return redirect("requests_app:received_requests")

@login_required
def cancel_request(request, request_id):
    item_request=get_object_or_404(ItemRequest,pk=request_id)
    if item_request.requester_id != request.user.id:
        return HttpResponseForbidden("You cannot cancel another user's request.")
    if request.method=="POST" and item_request.status==ItemRequest.STATUS_PENDING:
        item_request.status=ItemRequest.STATUS_CANCELLED
        item_request.save(update_fields=["status","updated_at"])
        messages.success(request,"Request cancelled.")
    return redirect("requests_app:my_requests")
