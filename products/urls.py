from django.urls import path
from .views import SubListView

app_name = 'products'
urlpatterns = [
    path('sub_list/', SubListView.as_view(), name='sub_list'),
]