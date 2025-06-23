from django.urls import path
from .views import TripSummaryView, GeneratePDF

urlpatterns = [
    path('summary/', TripSummaryView.as_view(), name='trip_summary'),
    path('summary/pdf/', GeneratePDF.as_view(), name='generate_pdf'),
]