"""Shopping Cart database layout"""

from django.contrib.auth.models import User
from django.db import models


class Customer(models.Model):
    user = models.ForeignKey(User)


class Merchant(models.Model):
    name = models.CharField(max_length=40)

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


class Item(models.Model):
    cart = models.ForeignKey(Cart)
    product = models.ForeignKey(Product)
    quantity = models.PositiveIntegerField()
