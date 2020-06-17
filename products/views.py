from products.managers import ProductManager
from products.forms import SearchForm
from django.shortcuts import render
from django.http import Http404, HttpResponse
from django.contrib.auth.decorators import login_required


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
    if request.method == "POST":
        form = SearchForm(request.POST)
        if form.is_valid():
            substitute, selected_product = ProductManager.search_from_user_input(
                form.cleaned_data
            )
            return render(
                request,
                "products/sub_list.html",
                {"product": substitute, "searched": selected_product},
            )
        else:
            print("form is not valid !")
            raise Http404
    else:
        form = SearchForm()
    return render(request, "products/sub_list.html", {"form": form})


@login_required
def save(request):
    if request.method == "POST":
        data = request.POST
        ProductManager.save_product(request, data)
        favs = ProductManager.get_fav(request)
        return render(request, "pages/myfood.html", {"favorites": favs})
    else:
        raise Http404


@login_required
def fav(request):
    favs = ProductManager.get_fav(request)
    return render(request, "pages/myfood.html", {"favorites": favs})


def detail(request):
    if request.method == "POST":
        data = request.POST
        product_detail = ProductManager.get_detail(data)
        return render(request, "pages/detail.html", {"product": product_detail})
    else:
        raise Http404
