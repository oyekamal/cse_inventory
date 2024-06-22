from django.contrib import admin

from .models import Equipment, Booking


@admin.register(Equipment)
class EquipmentAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "description",
        "available",
        "created_at",
        "updated_at",
    )
    list_filter = ("available", "created_at", "updated_at")
    search_fields = ("name",)
    date_hierarchy = "created_at"


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user",
        "equipment",
        "booking_date",
        "created_at",
        "updated_at",
    )
    list_filter = (
        "user",
        "equipment",
        "booking_date",
        "created_at",
        "updated_at",
    )
    date_hierarchy = "created_at"
