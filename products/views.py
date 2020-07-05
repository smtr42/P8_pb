from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render

from products.forms import SearchForm
from products.managers import ProductManager


def sub_list(request):
    if request.method == "POST":
        form = SearchForm(request.POST)
        if form.is_valid():
            (
                substitute,
                selected_product,
            ) = ProductManager.search_from_user_input(form.cleaned_data)
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


@login_required(login_url="/accounts/login/")
def save(request):
    if request.method == "POST":
        data = request.POST
        ProductManager.save_product(request, data)
        favs = ProductManager.get_fav(request)
        return render(request, "pages/myfood.html", {"favorites": favs})
    else:
        raise Http404


@login_required(login_url="/accounts/login/")
def fav(request):
    favs = ProductManager.get_fav(request)
    return render(request, "pages/myfood.html", {"favorites": favs})


def detail(request):
    if request.method == "POST":
        data = request.POST
        product_detail = ProductManager.get_detail(data)
        return render(
            request, "pages/detail.html", {"product": product_detail}
        )
    else:
        raise Http404
