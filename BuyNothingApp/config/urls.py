"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from .views import (
    home,
    login_view,
    register,
    profile,
    listings,
    listing_detail,
    create_listing,
    notifications,
    admin_dashboard,
    edit_profile,
)

urlpatterns = [
    path("admin/", admin.site.urls),

    path("", home, name="home"),
    path("login/", login_view, name="login"),
    path("register/", register, name="register"),
    path("profile/", profile, name="profile"),
    path("profile/edit/", edit_profile, name="edit_profile"),
    path("listings/", listings, name="listings"),
    path("listing/", listing_detail, name="listing_detail"),
    path("share/", create_listing, name="share"),
    path("notifications/", notifications, name="notifications"),
    path("admin-dashboard/", admin_dashboard, name="admin_dashboard"),
]