import datetime

import shopping_cart.models as models


CART_ID = 'CART-ID'


class Cart(object):

    def __init__(self, request):
        cart_id = request.session.get(CART_ID)
        if cart_id:
            try:
                cart = models.Cart.objects.get(id=cart_id,
                                               purchase_date__isnull=True)
            except models.Cart.DoesNotExist:
                cart = self.new(request)
        else:
            cart = self.new(request)
        self.cart = cart

    def __iter__(self):
        for item in self.cart.item_set.all():
            yield item

    def new(self, request):
        cart = models.Cart()
        cart.save()
        request.session[CART_ID] = cart.id
        return cart

    def add(self, product):
        item = models.Item()
        item.cart = self.cart
        item.product = product
        item.quantity = 1
        item.save()

    def clear(self):
        for item in self.cart.item_set:
            item.delete()

    def checkout(self, user):
        self.cart.customer = models.UserProfile.objects.get(user=user)
        self.cart.purchase_date = datetime.datetime.now()
        self.cart.save()
