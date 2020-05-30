from django.views.generic import TemplateView


class HomePageView(TemplateView):
    # https://docs.djangoproject.com/fr/2.2/topics/class-based-views/#subclassing-generic-views
    template_name = 'pages/index.html'