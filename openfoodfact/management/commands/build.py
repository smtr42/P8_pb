from django.core.management.base import BaseCommand
from ...utils import req_and_fill


class Command(BaseCommand):
    help = "Fetch data from OpenFoodFact API and build database"

    def handle(self, *args, **kwargs):
        req_and_fill()
