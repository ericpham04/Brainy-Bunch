from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from listings.models import Listing
from .forms import MessageForm
from .models import Message

@login_required
def inbox(request):
    qs=Message.objects.filter(receiver=request.user).select_related("sender","listing").order_by("-created_at")
    return render(request,"messages_app/inbox.html",{"received_messages":qs})

@login_required
def conversation(request,user_id,listing_id=None):
    other=get_object_or_404(User,pk=user_id)
    listing=get_object_or_404(Listing,pk=listing_id) if listing_id is not None else None
    qs=Message.objects.filter(Q(sender=request.user,receiver=other)|Q(sender=other,receiver=request.user))
    if listing is not None: qs=qs.filter(listing=listing)
    qs.filter(receiver=request.user,is_read=False).update(is_read=True)
    if request.method=="POST":
        form=MessageForm(request.POST)
        if form.is_valid():
            msg=form.save(commit=False); msg.sender=request.user; msg.receiver=other; msg.listing=listing; msg.save()
            messages.success(request,"Message sent.")
            if listing: return redirect("messages_app:conversation_with_listing",user_id=other.id,listing_id=listing.id)
            return redirect("messages_app:conversation",user_id=other.id)
    else: form=MessageForm()
    return render(request,"messages_app/conversation.html",{"other_user":other,"listing":listing,"conversation_messages":qs,"form":form})
