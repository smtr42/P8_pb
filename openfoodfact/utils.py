import requests


class RequestData:
    """ The class fetch the data and save it in to a json file"""

    def __init__(self):
        self.cat_url = "https://fr.openfoodfacts.org/categories.json"
        self.search_url = "https://fr.openfoodfacts.org/cgi/search.pl"
        self.list_cat = []
        self.list_prod = []

    def fetch_category(self):
        """Request the list of category from the API"""
        print("Getting Categories from API")
        try:
            response = self.req(self.cat_url)
            data = response.json()
            self.list_cat = [i['name'] for i in data['tags']]

        except requests.exceptions.Timeout as t:
            print("Request Timeout, please retry : ", t)
        except requests.exceptions.RequestException as err:
            print("Something went bad, please retry : :", err)
        # Reduce number of categories to limit database usage in heroku, now 10k -> 200

    def fetch_products(self):
        """Request the products in respect for the categories loaded"""
        print("Getting Products from API in respect to the Categories previously got")

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
                      "page_size": 1000,
                      # The API response in JSON
                      "json": 1}
            response = self.req(self.search_url, param=config)
            data = response.json()
            all_products[category] = data

        print("\n Raw data is now downloaded successfully")
        print("Now saving...")
        print("Success !")

    def req(self, url, param=None):
        """ small request function used multiple times"""
        response = requests.get(url, param)
        return response


def request_data():
    r = RequestData()
    r.fetch_category()
    r.fetch_products()
    return r.list_prod


if __name__ == "__main__":
    r = RequestData()
    r.fetch_category()
    print(len(r.list_cat))
