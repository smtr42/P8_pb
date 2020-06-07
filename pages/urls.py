from django.urls import path

from .views import HomePageView, NoticePageView

app_name = 'pages'
urlpatterns = [
    path('', HomePageView.as_view(), name='index'),
    path('notice', NoticePageView.as_view(), name='notice'),
]
