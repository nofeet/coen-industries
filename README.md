coen-industries
===============

A simple shopping cart application to help me learn Django.

It contains three merchant clients, each with product pages, a shopping cart and a checkout process to registered users. Each of these stores is on a subdomain.


### Merchants

* [Fargo Department Store](http://fargo-dept.coen.com:8000/shopping_cart)
* [Lebowski's](http://lebowskis.coen.com:8000/shopping_cart)
* [Soggy Bottom Boys](http://soggyboys.coen.com:8000/shopping_cart)

### Requirements

* Python 2.7
* Django 1.4

== Server Set-Up ==

Add these entries to your /etc/hosts file:

    127.0.0.1       coen.com 
    127.0.0.1       lebowskis.coen.com
    127.0.0.1       fargo-dept.coen.com
    127.0.0.1       not-a-merchant-test.coen.com
    127.0.0.1       soggyboys.coen.com

== Administration ==

Superuser--

    username: ecoen
    password: 1234
