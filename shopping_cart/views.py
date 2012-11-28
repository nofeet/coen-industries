from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render_to_response

from shopping_cart.cart import Cart
from shopping_cart.models import Product, Merchant



def index(request):
    """View for the Front page. Displays Product list."""
    merchant = Merchant.objects.get(name__iexact=u"Lebowski's")
    product_list = Product.objects.all()
    return render_to_response("shopping_cart/index.html",
                              {"merchant": merchant,
                               "product_list": product_list})


def detail(request, product_id):
    """View for a Product's detail page."""
    merchant = Merchant.objects.get(name__iexact=u"Lebowski's")
    product = Product.objects.get(id__exact=product_id)
    return render_to_response("shopping_cart/detail.html",
                              {"merchant": merchant,
                               "product": product})


def add_to_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    cart = Cart(request)
    cart.add(product)
    return redirect(view_cart)


def view_cart(request):
    continue_link = request.META.get('HTTP_REFERER','/shopping_cart/')
    return render_to_response('shopping_cart/cart.html',
                              {"cart": Cart(request),
                               "continue_link": continue_link})


@login_required
def checkout(request):
    return render_to_response("shopping_cart/checkout.html")