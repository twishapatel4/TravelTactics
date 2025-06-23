from django.db import models
from django.contrib.auth.models import User

class TouristLocation(models.Model):
    zone = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    name = models.CharField(max_length=255)
    location_type = models.CharField(max_length=100)
    establishment_year = models.IntegerField(blank=True, null=True)
    visit_duration_hours = models.FloatField(blank=True, null=True)
    google_rating = models.FloatField(default=3.0)
    entrance_fee = models.FloatField(blank=True, null=True)
    airport_within_city = models.BooleanField(default=False)
    weekly_off = models.CharField(max_length=100, blank=True, null=True)
    significance = models.CharField(max_length=255, blank=True, null=True)
    dslr_allowed = models.BooleanField(default=False)
    review_count = models.FloatField(blank=True, null=True)
    best_time_to_visit = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.name} - {self.city}, {self.state}"

class Itinerary(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    state = models.CharField(max_length=100, default="Gujarat")
    start_date = models.DateField()
    end_date = models.DateField()
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    locations = models.ManyToManyField(TouristLocation, related_name="itineraries", blank=True)

    def __str__(self):
        return f"{self.title} - {self.state}"
