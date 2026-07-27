from django.contrib import admin
from .models import ItemRequest

@admin.register(ItemRequest)
class ItemRequestAdmin(admin.ModelAdmin):
    list_display = ("listing","requester","status","created_at")
    list_filter = ("status","created_at")
    search_fields = ("listing__title","requester__username","message")
