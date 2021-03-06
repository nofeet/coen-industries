"""Shopping Cart database layout"""

from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save


class UserProfile(models.Model):
    user = models.OneToOneField(User)

    def __unicode__(self):
        return self.user.username

def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

post_save.connect(create_user_profile, sender=User)


class Merchant(models.Model):
    name = models.CharField(max_length=40)
    subdomain = models.CharField(max_length=15)
    admin = models.OneToOneField(User)

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
    customer = models.ForeignKey(UserProfile, blank=True, null=True)
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
