from django.conf.urls import patterns, url

urlpatterns = patterns("shopping_cart.views",
    url(r"^$", "index"),
    url(r"^view/(?P<product_id>\d+)/$", "detail"),
    url(r"^add/(?P<product_id>\d+)/$", "add_to_cart"),
    url(r"^view_cart/$", "view_cart"),
    url(r"^finalize/$", "finalize"),
    url(r"^checkout/$", "checkout"),
    url(r"^finish/$", "finish"),
    url(r'^register/$', 'register'),
)
