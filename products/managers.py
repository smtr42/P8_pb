"""Database operations with a global scale."""
from django.db import models
from django.apps import apps


class ProductManager(models.Manager):
    """Custom Object"""

    # def __init__(self):
    #     """Instanciate models used in the class."""
    #     self.product_model = apps.get_model('products', 'Product')
    #     self.category_model = apps.get_model('products', 'Category')
    #     self.favorite_model = apps.get_model('products', 'Favorite')

    def create_db_from_openfoodfacts(self, data):
        """Save each product into the database."""
        product_model = apps.get_model('products', 'Product')
        category_model = apps.get_model('products', 'Category')
        favorite_model = apps.get_model('products', 'Favorite')
        for category in data:
            cat = category_model(category_name=category)
            cat.save()
            for p in data[category]:
                prod = product_model(barcode=p['id'],
                                          product_name=p['product_name_fr'],
                                          nutriscore=p['nutrition_grade_fr'],
                                          url=p['url'],
                                          image_url=p['image_front_url'],
                                          image_nut_url=p[
                                              'image_ingredients_url'], )
                prod.save()
                prod.categories.add(cat)

    def delete_data_in_tables(self):
        """Delete data in tables but not tables. To use before insertion."""
        product_model = apps.get_model('products', 'Product')
        category_model = apps.get_model('products', 'Category')
        favorite_model = apps.get_model('products', 'Favorite')

        category_model.objects.all().delete()
        product_model.objects.all().delete()
        favorite_model.objects.all().delete()

    def get_substitutes_for_product(self, product):
        pass
