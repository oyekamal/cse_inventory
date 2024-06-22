from django.shortcuts import render
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Equipment, Booking
from .forms import BookingForm

# Create your views here.
def home(request):
    return render(request, "inventory/home.html")


class MyBookingsListView(LoginRequiredMixin, ListView):
    model = Booking
    template_name = 'inventory/my_bookings.html'
    context_object_name = 'bookings'

    def get_queryset(self):
        return Booking.objects.filter(user=self.request.user)

class EquipmentDetailView(LoginRequiredMixin, DetailView):
    model = Equipment
    template_name = 'inventory/equipment_detail.html'
    context_object_name = 'equipment'

class BookingCreateView(LoginRequiredMixin, CreateView):
    model = Booking
    form_class = BookingForm
    template_name = 'inventory/book_equipment.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.equipment = Equipment.objects.get(id=self.kwargs['pk'])
        equipment = form.instance.equipment
        equipment.available = False
        equipment.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('my_bookings')


class EquipmentListView(ListView):
    model = Equipment
    template_name = 'inventory/equipment_list.html'
    context_object_name = 'equipment'

    def get_queryset(self):
        return Equipment.objects.filter(available=True)
