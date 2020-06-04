from django.test import TestCase
from openfoodfact.utils import RequestData
from unittest.mock import Mock, patch
from unittest import mock


def fetch_cat_mock():
    return ["sabji"]


# def fetch_prod_mock():
#     return {'sabji': {'products': [
#         {'product_name_fr': 'Indisches Sabji', 'id': '4260155025099',
#          'image_ingredients_url': 'https://static.openfoodfacts.org/images/products/426/015/502/5099/ingredients_fr.10.400.jpg',
#          'image_front_url': 'https://static.openfoodfacts.org/images/products/426/015/502/5099/front_fr.7.400.jpg',
#          'nutrition_grade_fr': 'c',
#          'url': 'https://fr.openfoodfacts.org/produit/4260155025099/indisches-sabji-jooti'}],
#         'skip': 0, 'page': '1',
#         'page_size': '20',
#         'count': '1'}}


request_data = RequestData()

# with patch.object(request_data, '_fetch_products', fetch_prod_mock):
#     assert request_data.exec(20) == {'sabji': {'products': [
#         {'product_name_fr': 'Indisches Sabji', 'id': '4260155025099',
#          'image_ingredients_url': 'https://static.openfoodfacts.org/images/products/426/015/502/5099/ingredients_fr.10.400.jpg',
#          'image_front_url': 'https://static.openfoodfacts.org/images/products/426/015/502/5099/front_fr.7.400.jpg',
#          'nutrition_grade_fr': 'c',
#          'url': 'https://fr.openfoodfacts.org/produit/4260155025099/indisches-sabji-jooti'}],
#         'skip': 0, 'page': '1',
#         'page_size': '20',
#         'count': '1'}}

with patch.object(request_data, '_fetch_category', fetch_cat_mock):
    assert request_data.exec(20) == {'sabji': {'products': [
        {'product_name_fr': 'Indisches Sabji', 'id': '4260155025099',
         'image_ingredients_url': 'https://static.openfoodfacts.org/images/products/426/015/502/5099/ingredients_fr.10.400.jpg',
         'image_front_url': 'https://static.openfoodfacts.org/images/products/426/015/502/5099/front_fr.7.400.jpg',
         'nutrition_grade_fr': 'c',
         'url': 'https://fr.openfoodfacts.org/produit/4260155025099/indisches-sabji-jooti'}],
        'skip': 0, 'page': '1',
        'page_size': '20',
        'count': '1'}}
