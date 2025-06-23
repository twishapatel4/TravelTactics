from django.urls import path
from .views import (
    ItineraryListView, ItineraryDetailView,
    ItineraryCreateView, ItineraryUpdateView,
    ItineraryDeleteView
)
from django.contrib.auth.views import LoginView
from .views import ItineraryManageView
from .views import LocationListView


urlpatterns = [
    # path("locations/", LocationListView.as_view(), name="location_list"),
    # path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('', ItineraryListView.as_view(), name='itinerary_list'),  # List all itineraries
    path('<int:pk>/', ItineraryDetailView.as_view(), name='itinerary_detail'),  # View details
    path('new/', ItineraryCreateView.as_view(), name='itinerary_create'),  # Create new itinerary
    path('<int:pk>/edit/', ItineraryUpdateView.as_view(), name='itinerary_update'),  # Update itinerary
    path('<int:pk>/delete/', ItineraryDeleteView.as_view(), name='itinerary_delete'),  # Delete itinerary
    path('itinerary/<int:pk>/manage/', ItineraryManageView.as_view(), name='manage_itinerary'),
]
