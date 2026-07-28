from django.shortcuts import render

def home(request):
    return render(request, "home.html")

def login_view(request):
    return render(request, "login.html")

def register(request):
    return render(request, "register.html")

def create_listing(request):
    return render(request, "create_listing.html")

def profile(request):
    return render(request, "profile.html")

def listings(request):
    return render(request, "listings.html")

def listing_detail(request):
    return render(request, "listing_detail.html")

def notifications(request):
    return render(request, "notifications.html")

def admin_dashboard(request):
    context = {
        "total_users": 24,
        "total_listings": 18,
        "pending_users": 3,
        "reported_listings": 2,
    }
    return render(request, "admin_dashboard.html", context)