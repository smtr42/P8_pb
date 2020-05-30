from django.urls import path
from .views import search_product

app_name = 'products'
urlpatterns = [
    path('', search_product, name='sub_list'),
]