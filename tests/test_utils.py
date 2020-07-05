import unittest
from unittest import mock, skip
from unittest.mock import Mock, patch

from django.test import TestCase

from openfoodfact.utils import RequestData


# @skip("skip the test")
class UtilsTest(TestCase):
    def test_product_request(self):
        def fetch_cat_mock():
            return ["sabji"]

        request_data = RequestData()

        with patch.object(request_data, "_fetch_category", fetch_cat_mock):
            self.assertIsInstance(request_data.exec(20), dict)
            self.assertEqual(
                request_data.exec(20)["sabji"]["products"][0][
                    "product_name_fr"
                ],
                "Indisches Sabji",
            )
            self.assertEqual(
                request_data.exec(20),
                {
                    "sabji": {
                        "products": [
                            {
                                "product_name_fr": "Indisches Sabji",
                                "id": "4260155025099",
                                "image_ingredients_url": "https://static.openfoodfacts.org/images/products/426/015/502/5099/ingredients_fr.10.400.jpg",
                                "image_front_url": "https://static.openfoodfacts.org/images/products/426/015/502/5099/front_fr.7.400.jpg",
                                "nutrition_grade_fr": "c",
                                "url": "https://fr.openfoodfacts.org/produit/4260155025099/indisches-sabji-jooti",
                            }
                        ],
                        "skip": 0,
                        "page": "1",
                        "page_size": "20",
                        "count": 1,
                    }
                },
            )

    def test_category_request(self):
        def fetch_products_mock(*args, **kwargs):
            return {
                "sabji": {
                    "products": [
                        {
                            "product_name_fr": "Indisches Sabji",
                            "id": "4260155025099",
                            "image_ingredients_url": "https://static.openfoodfacts.org/images/products/426/015/502/5099/ingredients_fr.10.400.jpg",
                            "image_front_url": "https://static.openfoodfacts.org/images/products/426/015/502/5099/front_fr.7.400.jpg",
                            "nutrition_grade_fr": "c",
                            "url": "https://fr.openfoodfacts.org/produit/4260155025099/indisches-sabji-jooti",
                        }
                    ],
                    "skip": 0,
                    "page": "1",
                    "page_size": "20",
                    "count": 1,
                }
            }

        request_data = RequestData()

        with patch.object(
            request_data, "_fetch_products", fetch_products_mock
        ):
            self.assertIsInstance(request_data.exec(20), dict)
            self.assertEqual(
                request_data.list_cat,
                [
                    "Aliments et boissons à base de végétaux",
                    "Aliments d'origine végétale",
                    "Snacks",
                    "Snacks sucrés",
                    "Boissons",
                    "Produits laitiers",
                    "Viandes",
                    "Aliments à base de fruits et de légumes",
                    "Plats préparés",
                    "Céréales et pommes de terre",
                    "Produits fermentés",
                    "Produits laitiers fermentés",
                    "Produits à tartiner",
                    "Biscuits et gâteaux",
                    "Charcuteries",
                    "Epicerie",
                    "Petit-déjeuners",
                ],
            )
