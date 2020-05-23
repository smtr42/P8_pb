from django.urls import path

# from . import views
#
# urlpatterns = [
#     path('', views.HomePageView.as_view(), name='index'),
# ]

from . import views
app_name = 'pages'

urlpatterns = [
    path('', views.index, name='index'),
]