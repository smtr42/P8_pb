from django.urls import path
from .views import sub_list, save

app_name = 'products'
urlpatterns = [
    path("", sub_list, name="sub_list"),
    path("<int:product_id>", save, name="save")
]