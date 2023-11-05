from django.core.management.base import BaseCommand
from stores.models import Orders
from ecsite_project.settings import BASE_DIR
import os
import csv

class Command(BaseCommand):

    def handle(self, *args, **options):
        orders = Orders.objects.all()

        return super().handle(*args, **options)