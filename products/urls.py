from django.urls import path
from .views import search_product
from .views import home

app_name = 'products'
urlpatterns = [
    # path('', search_product, name='sub_list'),
    path("", home, name="home")
]
