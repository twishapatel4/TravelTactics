from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView, FormView
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Itinerary, TouristLocation
from .forms import ItineraryForm, LocationSelectionForm

class ItineraryListView(LoginRequiredMixin, ListView):
    model = Itinerary
    template_name = 'itinerary_list.html'
    context_object_name = 'itineraries'

    def get_queryset(self):
        return Itinerary.objects.filter(user=self.request.user)

class ItineraryDetailView(LoginRequiredMixin, DetailView):
    model = Itinerary
    template_name = 'itinerary_detail.html'
    context_object_name = 'itinerary'

class ItineraryCreateView(LoginRequiredMixin, CreateView):
    model = Itinerary
    form_class = ItineraryForm
    template_name = 'itinerary_form.html'
    success_url = reverse_lazy('itinerary_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class ItineraryUpdateView(LoginRequiredMixin, UpdateView):
    model = Itinerary
    form_class = ItineraryForm
    template_name = 'itinerary_form.html'
    success_url = reverse_lazy('itinerary_list')

class ItineraryDeleteView(LoginRequiredMixin, DeleteView):
    model = Itinerary
    template_name = 'itinerary_confirm_delete.html'
    success_url = reverse_lazy('itinerary_list')

class ItineraryManageView(LoginRequiredMixin, FormView):
    template_name = 'manage_itinerary.html'
    form_class = LocationSelectionForm

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        self.itinerary = get_object_or_404(Itinerary, pk=self.kwargs['pk'], user=self.request.user)
        kwargs['itinerary'] = self.itinerary
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['itinerary'] = self.itinerary
        context['all_locations'] = TouristLocation.objects.filter(state=self.itinerary.state)
        return context

    def form_valid(self, form):
        selected_locations = form.cleaned_data['locations']
        self.itinerary.locations.set(selected_locations)
        return redirect('itinerary_detail', pk=self.itinerary.pk)

class LocationListView(ListView):
    model = TouristLocation
    template_name = 'location_list.html'
    context_object_name = 'locations'