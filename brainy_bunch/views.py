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