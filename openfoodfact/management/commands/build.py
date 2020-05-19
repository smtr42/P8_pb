from django.core.management.base import BaseCommand
from ...utils import request_data


class Command(BaseCommand):
    help = "Fetch data from OpenFoodFact API and build database"

    def handle(self, *args, **kwargs):
        data = request_data()

        pass
