"""Database operations with a global scale."""
from django.db import models
from django.apps import apps
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
        """Retrieve substitute from user search."""
        # https://docs.djangoproject.com/fr/3.0/ref/models/querysets/#field-lookups

        product_model = apps.get_model('products', 'Product')
        name = data['product']

        selected_product = (product_model.objects.filter(
            product_name__iexact=name).values())
        selected_product_category_name = product_model.objects.filter(product_name__iexact=name).values('categories__category_name')


        # substitutes = (product_model.objects.filter(
        #     categories__id=selected_product[0][
        #         'category'])
        #                    .order_by('nutriscore', 'popularity').values(
        #     'name', 'nutriscore', 'pk', 'img_url')[:12])

        # substitutes = (product_model.objects.filter(
        #     categories__id=selected_product[0][
        #         'category'])
        #                    .order_by('nutriscore', 'popularity').values(
        #     'name', 'nutriscore', 'pk', 'img_url')[:12])

        # if selected_product.nutriscore == "a":
        #     print("nutriscore = A")
        # substitute_list = get_list_or_404(
        #     product_model.objects.order_by('nutriscore'),
        #                 categories=product_model.categories,
        #                 nutriscore__gt="B")

        # dictio = {"product": selected_product}

        return selected_product

    #         search_product = (Product.objects.filter(name__icontains=input)
    #                           .order_by('nutriscore').values('name', 'category', 'img_url', 'pk')[:1])
    #         if search_product:
    #             products = (Product.objects.filter(category__id=search_product[0]['category'])
    #                         .order_by('nutriscore', 'popularity').values('name', 'nutriscore', 'pk', 'img_url')[:12])
    #             search_product_status = True
    #             search_product = search_product[0]

    def get_all_by_term(self, term):
        return self.filter(product_name__icontains=term)

    # select_related

    # Sélectionner les produits ayant un meilleur nutriscore
    # et qui ont des catégories en commun, ordonnés par nombre
    # décroissant de catégories partagées.
    #
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

    def get_substitute_from_product(self):
        pass

    def get_product_from_selection(self):
        pass