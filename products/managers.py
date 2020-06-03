"""Database operations with a global scale."""
from django.db import models
from django.apps import apps
from django.shortcuts import get_list_or_404
from django.db import IntegrityError
from django.core.management.color import no_style
from django.db import connection

class ProductManager(models.Manager):
    """Custom Object"""

    def create_db_from_openfoodfacts(self, data):
        """Save each product into the database."""
        product_model = apps.get_model('products', 'Product')
        category_model = apps.get_model('products', 'Category')
        print("Saving data into the database")
        for category in data:
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
        sequence_sql = connection.ops.sequence_reset_sql(no_style(),
                                                         [product_model, category_model, favorite_model])
        with connection.cursor() as cursor:
            for sql in sequence_sql:
                cursor.execute(sql)


    @staticmethod
    def search_from_user_input(data):
        """Retrieve products from user search."""
        # https://docs.djangoproject.com/fr/3.0/ref/models/querysets/#field-lookups

        product_model = apps.get_model('products', 'Product')

        exact_query = product_model.objects.filter(
            product_name__iexact=data['product'])
        contain_query = product_model.objects.filter(
                product_name__icontains=data['product'])

        search_result = [contain_query if not exact_query else exact_query]

        # full_prod = get_list_or_404(
        # product_model.objects.order_by('nutriscore'))

        mydict = {"product": search_result}
        # mydict = {"product": full_prod}
        print(search_result)
        return mydict

# select_related


# Sélectionner les produits ayant un meilleur nutriscore
# et qui ont des catégories en commun, ordonnés par nombre
# décroissant de catégories partagées.

#         ''' Get the most accurate healthy substitutes for
#             a given search_product and a category.
#         '''
#         rows = self.database.query(
#             "SELECT "
#             "    P.id as Id, "
#             "    P.product_name as Name, "
#             "    P.nutriscore as Nutriscore "
#             "FROM Product P "
#             "INNER JOIN Product_Category AS PC "
#             "    ON P.id = PC.id_product "
#             "INNER JOIN Product_Category AS PC2 "
#             "    ON P.id = PC2.id_product "
#             "INNER JOIN Product_Category AS PC3 "
#             "    ON PC2.id_category = PC3.id_category "
#             "WHERE P.nutriscore in ('a', 'b') "
#             "AND PC.id_category = :cat_id "
#             "AND PC3.id_product = :p_id "
#             "GROUP BY P.id, P.product_name, P.nutriscore "
#             "ORDER BY P.nutriscore ASC, COUNT(PC2.id_category) DESC "
#             "LIMIT 5 ",
#             cat_id=id_category,
#             p_id=id_search_product)