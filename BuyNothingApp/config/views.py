from django.shortcuts import render

def home(request):
    return render(request, "create_listing.html")

def listings(request):
    return render(request, "create_listing.html")

def profile(request):
    return render(request, "create_listing.html")

def notifications(request):
    return render(request, "create_listing.html")

def create_listing(request):
    return render(request, "create_listing.html")