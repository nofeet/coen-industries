from django.contrib import admin

from shopping_cart.models import Cart, UserProfile, Product, Merchant


class MerchantAdmin(admin.ModelAdmin):
    list_display = ("name", "subdomain", "admin")


class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "merchant", "price")


admin.site.register(Cart)
admin.site.register(UserProfile)
admin.site.register(Merchant, MerchantAdmin)
admin.site.register(Product, ProductAdmin)
