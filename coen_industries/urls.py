"""Project URLconf"""

from django.conf.urls import include, patterns, url
from django.contrib import admin


admin.autodiscover()

urlpatterns = patterns('',
    url(r'^shopping_cart/', include('shopping_cart.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
