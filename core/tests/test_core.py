from pytest import mark
from django.urls import reverse
from django.contrib.staticfiles import finders

common_args = (
    "url, status,",
    [
        ("/badurl/", 404),
        (reverse("admin:index"), 302),
        (reverse("users:signup"), 200),
        (reverse("products:sub_list"), 200),
        (reverse("products:save"), 302),
        (reverse("products:fav"), 302),
        (reverse("products:detail"), 404),
        (reverse("pages:index"), 200),
        (reverse("pages:notice"), 200),
        (reverse("pages:profile"), 200),
        (reverse("pages:myfood"), 200),
    ],
)

static_files = (
    "static_path",
    [("dist/css/styles.css"), ("dist/js/scripts.js"), ("dist/assets/img/a.png")],
)


@mark.parametrize(*common_args)
@mark.django_db
@mark.urls("core.urls")
def test_route(client, url, status):
    response = client.get(url)
    assert response.status_code == status


@mark.parametrize(*static_files)
def test_static_files(static_path):
    assert finders.find(static_path) is not None
