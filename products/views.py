from products.managers import ProductManager
from products.forms import SearchForm
from django.shortcuts import render
from django.http import Http404


# def search_product(request):
#     # if this is a POST request we need to process the form data
#     if request.method == 'GET':
#         # create a form instance and populate it with data from the request:
#         form = SearchForm(request.GET)
#         # check whether it's valid:
#         if form.is_valid():
#             data = ProductManager.search_from_user_input(
#                 form.cleaned_data)
#             return render(request, 'products/sub_list.html', data)
#             # return HttpResponseRedirect('products/sub_list.html')
#         else:
#             raise Http404
#     # if a GET (or any other method) we'll create a blank form
#     else:
#         form = SearchForm()
#     return render(request, 'products/sub_list.html', {'form': form})


def sub_list(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            data = ProductManager.search_from_user_input(form.cleaned_data)
            return render(request, 'products/sub_list.html', {"product": data})
        else:
            print("form is not valid !")
            raise Http404
    else:
        form = SearchForm()
    return render(request, 'products/sub_list.html', {'form': form})

