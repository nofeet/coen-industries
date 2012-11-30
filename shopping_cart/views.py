from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import redirect, render_to_response
from django.template.context import RequestContext

from shopping_cart.cart import Cart
from shopping_cart.models import Product, Merchant


def index(request):
    """View for the Front page. Displays Product list."""
    try:
        merchant = Merchant.objects.get(subdomain__iexact=request.subdomain)
    except Merchant.DoesNotExist:
        # not on a merchant subdomain
        raise Http404
    product_list = Product.objects.filter(merchant=merchant)
    return render_to_response("shopping_cart/index.html",
                              {"merchant": merchant,
                               "product_list": product_list})


def detail(request, product_id):
    """View for a Product's detail page."""
    try:
        merchant = Merchant.objects.get(subdomain__iexact=request.subdomain)
    except Merchant.DoesNotExist:
        # not on a merchant subdomain
        raise Http404
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
def finalize(request):
    return render_to_response("shopping_cart/finalize.html",
                              {"cart": Cart(request)},
                              context_instance=RequestContext(request))


@login_required
def checkout(request):
    cart = Cart(request)
    cart.checkout(request.user)
    return HttpResponseRedirect(reverse('shopping_cart.views.finish'))


def finish(request):
    return render_to_response("shopping_cart/finish.html",
                              {"cart": Cart(request).cart})


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/shopping_cart/")
    else:
        form = UserCreationForm()
    return render_to_response("shopping_cart/register.html",
                              {"form": form},
                              context_instance=RequestContext(request))
