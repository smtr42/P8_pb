"""Database operations with a global scale."""
from django.db import models
from django.apps import apps
from django.shortcuts import get_list_or_404
from django.db import IntegrityError


class ProductManager(models.Manager):
    """Custom Object"""

    def create_db_from_openfoodfacts(self, data):
        """Save each product into the database."""
        product_model = apps.get_model('products', 'Product')
        category_model = apps.get_model('products', 'Category')
        for category in data:
            print("Saving in database the Category : ", category)
            cat = category_model(category_name=category)
            cat.save()
            for p in data[category]:
                try:
                    prod = product_model(barcode=p['id'],
                                         product_name=p['product_name_fr'],
                                         nutriscore=p['nutrition_grade_fr'],
                                         url=p['url'],
                                         image_url=p['image_front_url'],
                                         image_nut_url=p[
                                             'image_ingredients_url'], )
                    prod.save()
                    prod.categories.add(cat)
                except IntegrityError:
                    pass

    def delete_data_in_tables(self):
        """Delete data in tables but not tables. To use before insertion."""
        product_model = apps.get_model('products', 'Product')
        category_model = apps.get_model('products', 'Category')
        favorite_model = apps.get_model('products', 'Favorite')
        print("Deleting everything in database")
        category_model.objects.all().delete()
        product_model.objects.all().delete()
        favorite_model.objects.all().delete()

    @staticmethod
    def get_substitutes_for_product(data):
        """Retrieve products from user search."""
        product_model = apps.get_model('products', 'Product')

        exact_query = product_model.objects.filter(
            product_name__iexact=data['product'])
        contain_query = product_model.objects.filter(
            product_name__icontains=data['product'])
        search_result = [
            list(contain_query) if not exact_query else list(exact_query)]
        nit_substitute_list = get_list_or_404(
            product_model.objects.order_by('nutriscore'),
            category=product_model.categories,
            nutrition_score__lt=product_model.nutriscore)
        print("final_search : ", nit_substitute_list)
        return nit_substitute_list
