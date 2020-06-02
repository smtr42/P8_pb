# from django.views.generic import ListView
# from products.models import Product
from products.managers import ProductManager
from products.forms import SearchForm
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import Http404


def search_product(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = SearchForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            data = ProductManager.search_from_user_input(
                form.cleaned_data)
            return render(request, 'products/search_list.html', data)
            # return HttpResponseRedirect('products/sub_list.html')
        else:
            raise Http404
    # if a GET (or any other method) we'll create a blank form
    else:
        form = SearchForm()
    return render(request, 'products/search_list.html', {'form': form})


def home(request):
    return render(request, "pages/index.html")
