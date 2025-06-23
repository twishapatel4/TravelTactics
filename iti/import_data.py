import os
import sys
import django
import csv

# ✅ Setup Django
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  # Adds project root to Python path
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'TT.settings')  # 🔁 Replace with your actual project name
django.setup()

# ✅ Now you can import models
from iti.models import TouristLocation
from django.conf import settings

# Get absolute path of CSV file
BASE_DIR = settings.BASE_DIR
csv_path = os.path.join(BASE_DIR, "cleaned_dataset.csv")

def import_locations():
    with open(csv_path, newline='', encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        locations = []

        for row in reader:
            location = TouristLocation(
                zone=row["Zone"].strip() if row.get("Zone") else None,
                state=row["State"].strip(),
                city=row["City"].strip(),
                name=row["Name"].strip(),
                location_type=row["location_type"].strip(),
                establishment_year=int(row["establishment_year"]) if row["establishment_year"].isdigit() else None,
                visit_duration_hours=float(row["visit_duration_hours"]) if row["visit_duration_hours"] else None,
                google_rating=float(row["google_rating"]) if row["google_rating"] else None,
                entrance_fee=row["entrance_fee"].strip() if row.get("entrance_fee") else None,
                airport_within_city=row["airport_within_city"].strip().lower() == "yes",
                weekly_off=row["weekly_off"].strip() if row.get("weekly_off") else None,
                significance=row["significance"].strip() if row.get("significance") else None,
                dslr_allowed=row["dslr_allowed"].strip().lower() == "yes",
                # number_of_visitors=float(row["review_count",0]) if row["review_count"] else None,
                best_time_to_visit=row["best_time_to_visit"].strip() if row.get("best_time_to_visit") else None,
            )
            locations.append(location)

        TouristLocation.objects.bulk_create(locations)
        print(f"✅ Successfully imported {len(locations)} locations.")

# Run the import
if __name__ == "__main__":
    import_locations()
