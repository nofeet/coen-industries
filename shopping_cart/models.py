"""Shopping Cart database layout"""

from django.contrib.auth.models import User
from django.db import models


class Customer(models.Model):
    user = models.ForeignKey(User)

    def __unicode__(self):
        return self.user.username


class Merchant(models.Model):
    name = models.CharField(max_length=40)
    subdomain = models.CharField(max_length=15)

    def __unicode__(self):
        return self.name


class Product(models.Model):
    merchant = models.ForeignKey(Merchant)
    name = models.CharField(max_length=40)
    description = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        ordering = ["name"]

    def __unicode__(self):
        return self.name


class Cart(models.Model):
    # These fields will be set if purchase is completed by authenticated user
    customer = models.ForeignKey(Customer, blank=True, null=True)
    purchase_date = models.DateTimeField(blank=True, null=True)

    def __unicode__(self):
        ustr = u"id %d" % self.id
        if self.purchase_date:
            ustr += u" (purchased on %s)" % self.purchase_date
        return ustr


class Item(models.Model):
    cart = models.ForeignKey(Cart)
    product = models.ForeignKey(Product)
    quantity = models.PositiveIntegerField()
