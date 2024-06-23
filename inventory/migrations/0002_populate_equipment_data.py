# inventory/migrations/0002_populate_equipment_data.py

from django.db import migrations
from django.utils import timezone


def create_equipment_data(apps, schema_editor):
    Equipment = apps.get_model("inventory", "Equipment")
    equipment_list = [
        {
            "name": "Laptop",
            "description": "A high-performance laptop with a 15-inch display.",
            "available": True,
        },
        {
            "name": "Printer",
            "description": "A wireless printer suitable for home office use.",
            "available": False,
        },
        {
            "name": "Headphones",
            "description": "Noise-cancelling headphones for long flights.",
            "available": True,
        },
    ]

    for item in equipment_list:
        Equipment.objects.create(
            name=item["name"],
            description=item["description"],
            available=item["available"],
            created_at=timezone.now(),
            updated_at=timezone.now(),
        )


class Migration(migrations.Migration):

    dependencies = [
        (
            "inventory",
            "0001_initial",
        ),  # This should match the initial migration filename
    ]

    operations = [
        migrations.RunPython(create_equipment_data),
    ]
