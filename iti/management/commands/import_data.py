import csv
import os
from django.core.management.base import BaseCommand, CommandError
from iti.models import TouristLocation

class Command(BaseCommand):
    help = 'Import tourist locations from cleaned_dataset.csv'

    def handle(self, *args, **kwargs):
        csv_file = os.path.join(os.getcwd(), 'cleaned_dataset.csv')

        if not os.path.exists(csv_file):
            raise CommandError(f"File {csv_file} does not exist")

        with open(csv_file, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            locations = []

            for row in reader:
                try:
                    location = TouristLocation(
                        zone=row.get('Zone') or None,
                        state=row['State'],
                        city=row['City'],
                        name=row['Name'],
                        location_type=row['location_type'],
                        establishment_year=self.safe_int(row.get('establishment_year')),
                        visit_duration_hours=self.safe_float(row.get('visit_duration_hours')),
                        google_rating=self.safe_float(row.get('google_rating'), 3.0),
                        entrance_fee=self.safe_float(row.get('entrance_fee')),
                        airport_within_city=row.get('airport_within_city', 'False') == 'TRUE',
                        weekly_off=row.get('weekly_off') or None,
                        significance=row.get('Significance') or None,
                        dslr_allowed=row.get('dslr_allowed', 'False') == 'TRUE',
                        review_count=self.safe_float(row.get('reviewCount')),
                        best_time_to_visit=row.get('best_time_to_visit') or None
                    )
                    locations.append(location)
                except Exception as row_error:
                    self.stdout.write(self.style.WARNING(f"Skipping row due to error: {row_error}"))

            TouristLocation.objects.bulk_create(locations)
            self.stdout.write(self.style.SUCCESS(f"Successfully imported {len(locations)} locations."))

    def safe_int(self, value, default=None):
        try:
            return int(value)
        except (TypeError, ValueError):
            return default

    def safe_float(self, value, default=None):
        try:
            return float(value)
        except (TypeError, ValueError):
            return default
