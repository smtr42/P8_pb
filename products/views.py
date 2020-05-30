from django.shortcuts import render
from django.views.generic import ListView
from django.utils import timezone
from products.models import Product

# Create your views here.
class SubListView(ListView):
    model = Product
    template_name = "products/sub_list.html"
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context
