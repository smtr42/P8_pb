from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Fetch data from OpenFoodFact API and build database"

    def handle(self, *args, **kwargs):
        pass
