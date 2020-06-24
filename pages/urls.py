from django.urls import path

from .views import HomePageView, MyFood, NoticePageView, Profile

app_name = "pages"
urlpatterns = [
    path("", HomePageView.as_view(), name="index"),
    path("notice", NoticePageView.as_view(), name="notice"),
    path("profile", MyFood.as_view(), name="profile"),
    path("myfood", Profile.as_view(), name="myfood"),
]
