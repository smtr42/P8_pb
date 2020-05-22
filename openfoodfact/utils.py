import requests

from products.models import Product, Category, Favorite


class RequestData:
    """The class fetch the data and save it in to a json file."""

    def __init__(self):
        self.cat_url = "https://fr.openfoodfacts.org/categories.json"
        self.search_url = "https://fr.openfoodfacts.org/cgi/search.pl"
        self.list_cat = []
        self.list_prod = []
        self.data = {}

    def exec(self):
        """Main public function executing all necessary privates functions."""
        self._fetch_category()
        data = self._fetch_products()
        return data

    def _fetch_category(self):
        """Request the list of category from the API."""
        print("Getting Categories from API")
        try:
            response = self._req(self.cat_url)
            data = response.json()
            self.list_cat = [i['name'] for i in data['tags']]
            self.list_cat = self.list_cat[:1]
            self.data = {}

        except requests.exceptions.Timeout as t:
            print("Request Timeout, please retry : ", t)
        except requests.exceptions.RequestException as err:
            print("Something went bad, please retry : :", err)

    def _fetch_products(self):
        """Request the products in respect for the categories loaded"""
        print("Getting Products from API in respect to the"
              " Categories previously got")
        all_products = {}
        for category in self.list_cat:
            config = {"action": "process",
                      # Get the result by category
                      "tagtype_0": "categories",
                      # the tag represents the article search
                      'tag_0': category,
                      "tag_contains_0": "contains",
                      # Number of articles per page
                      # Min content 20, Max content 1000
                      "page_size": 20,  # to modify to 250
                      # The API response in JSON
                      "json": 1}
            response = self._req(self.search_url, param=config)
            data = response.json()
            all_products[category] = data
        return all_products

    def _req(self, url, param=None):
        """Small request function used multiple times."""
        response = requests.get(url, param)
        return response


class Cleaner:
    """This class will handle the data formatting before db use."""

    def __init__(self, data):
        """Initialize variables and launch filter_products"""
        self.data = data
        self.keys = ['id', 'product_name_fr', 'nutrition_grade_fr',
                     'url', 'image_front_url', 'image_ingredients_url', ]
        self.list_cat = [categories for categories in self.data]
        self._dict_data = {}
        self.list_of_dictio = []
        self.barcode_list = []

    def filter_product(self):
        """Get the data from json files and run checks"""
        for category in self.list_cat:
            for element in self.data[category]['products']:
                if self._data_exist(element):
                    self._data_format(element, category)
        return self._dict_data

    def _data_exist(self, element):
        """Run trough the data, if something's missing it's discarded."""
        for x in self.keys:
            if x not in element or element[x] == "" \
                    or len(element["id"]) != 13:
                return False
        barcode = int(element['id'])
        if barcode not in set(self.barcode_list):
            self.barcode_list.append(barcode)
        else:
            return False
        return True

    def _data_format(self, element, cat):
        """Format the data so it's usable into a list of dictionary
        It returns data that will be used for the database."""

        dictio = {}
        for key in self.keys:
            dictio[key] = element[key]
        # self._dict_data.append(dictio)
        self.list_of_dictio.append(dictio)
        self._dict_data[cat] = self.list_of_dictio


class DbFiller:
    """Handle the filling of the database."""

    def __init__(self, data):
        self.data = data

    def _fill_categories(self):
        categories = [categories for categories in self.data]
        for category in categories:
            cat = Category(category_name=category)
            cat.save()

    def _fill_products(self):

        pass


def req_and_fill():
    """Main function to instantiate and launch operations."""
    r = RequestData()
    data = r.exec()
    c = Cleaner(data)
    data = c.filter_product()
    print(data)
    # d = DbFiller(data)
    # d._fill_categories()
    # return data


if __name__ == "__main__":
    req_and_fill()
