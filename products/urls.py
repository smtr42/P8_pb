from django.urls import path
from .views import sub_list

app_name = 'products'
urlpatterns = [
    path("", sub_list, name="sub_list")
]