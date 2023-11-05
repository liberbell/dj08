from django.core.management.base import BaseCommand
from stores.models import Orders
from ecsite_project.settings import BASE_DIR
import os
import csv
from datetime import datetime

class Command(BaseCommand):

    def handle(self, *args, **options):
        orders = Orders.objects.all()
        file_path = os.path.join(BASE_DIR, "output", "orders", f"orders_{datetime.now().strftime('%Y%m%d%H%M%S')}")
        with open(file_path, mode="w", newline="\n", encoding="utf-8") as csv_file:
            field_name = ["id", "user", "address", "total_price"]
            writer = csv.DictWriter(csv_file, fieldnames=field_name)
            writer.writeheader()

        return super().handle(*args, **options)