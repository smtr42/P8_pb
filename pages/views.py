from django.views.generic import TemplateView


class HomePageView(TemplateView):
    # https://docs.djangoproject.com/fr/2.2/topics/class-based-views/#subclassing-generic-views
    template_name = "pages/index.html"


class NoticePageView(TemplateView):
    template_name = "pages/notice.html"


class MyFood(TemplateView):
    template_name = "pages/myfood.html"


class Profile(TemplateView):
    template_name = "pages/profile.html"
