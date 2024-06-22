from django.urls import include, path
from . import views
from django.urls import path
from .views import (
    EquipmentListView,
    EquipmentDetailView,
    BookingCreateView,
    MyBookingsListView,
)

urlpatterns = [
    path("", views.home, name="home"),
    path("equipments/", EquipmentListView.as_view(), name="equipment_list"),
    path("equipment/<int:pk>/", EquipmentDetailView.as_view(), name="equipment_detail"),
    path(
        "equipment/<int:pk>/book/", BookingCreateView.as_view(), name="book_equipment"
    ),
    path("my_bookings/", MyBookingsListView.as_view(), name="my_bookings"),
]
