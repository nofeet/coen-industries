"""Test cases for shopping cart application."""

from httplib import NOT_FOUND, OK

from django.core.urlresolvers import reverse
from django.http import HttpRequest
from django.test import TestCase

from shopping_cart.cart import Cart, CART_ID
from shopping_cart.models import Product



#--- Constants
BAD_SUBDOMAIN_URL = "not-a-merchant-test.coen.com"
GOOD_SUBDOMAIN_URL = "lebowskis.coen.com"
GOOD_CART_ID = "1"
GOOD_PRODUCT_ID = "2"


class ShoppingCartViewsTestCases(TestCase):
    """Test cases for the shopping_cart views."""

    fixtures = ["shopping_cart.json"]
    longMessage = True

    def test_index_page_contents(self):
        """Verify the contents of the index page appear correctly."""
        resp = self.client.get(reverse("shopping_cart.views.index"),
                               HTTP_HOST=GOOD_SUBDOMAIN_URL)

        self.assertEqual(resp.status_code, OK,
                         "Status code for Index page on valid subdomain")
        self.assertTrue("product_list" in resp.context)

        expected_num_products = 3
        actual_num_products = len(resp.context["product_list"])
        self.assertEqual(expected_num_products, actual_num_products,
                         "Number of products on front page")

    def test_bad_merchant_404(self):
        """Verify going to shopping_cart home for invalid merchant -> 404."""
        resp = self.client.get(reverse("shopping_cart.views.index"),
                               HTTP_HOST=BAD_SUBDOMAIN_URL)
        self.assertEqual(resp.status_code, NOT_FOUND,
                         "Status code for Index page when bad subdomain given")

    def test_no_subdomain_404(self):
        """Verify going to shopping_cart home with no subdomain -> 404."""
        resp = self.client.get(reverse("shopping_cart.views.index"))
        self.assertEqual(resp.status_code, NOT_FOUND,
                         "Status code for Index page when no subdomain given")


class CartTestCases(TestCase):
    """Test cases for the app's Cart class."""

    fixtures = ["shopping_cart.json"]
    longMessage = True

    def test_new_cart(self):
        """Verify a new cart can be created."""
        # create a mock request
        test_request = HttpRequest()
        test_request.session = {}
        cart = Cart(test_request)
        self.assertListEqual([], list(cart.cart.item_set.all()),
                             "Item list in new cart")

    def test_fetching_cart(self):
        """Verify an existing cart is fetched instead of reinstantiated."""
        test_request = HttpRequest()
        test_request.session = {CART_ID: GOOD_CART_ID}
        cart = Cart(test_request)
        expected_num_items = 3
        actual_num_items = len(cart.cart.item_set.all())
        self.assertEqual(expected_num_items, actual_num_items,
                         "Number of items in refetched cart")

    def test_add_to_cart(self):
        """Verify items are added to a cart properly."""
        test_request = HttpRequest()
        test_request.session = {}
        cart = Cart(test_request)
        product = Product.objects.get(id=GOOD_PRODUCT_ID)
        cart.add(product)
        expected_num_items = 1
        actual_num_items = len(cart.cart.item_set.all())
        self.assertEqual(expected_num_items, actual_num_items,
                         "Number of items after adding 1 to empty cart")
