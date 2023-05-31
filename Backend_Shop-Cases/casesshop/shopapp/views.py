from django.shortcuts import render

from shopapp.models import *


# Create your views here.


def index(requests):
    home_order = Orders.objects.all()
    home_photo_title = Index_Phonto.objects.all()

    ctx = {
        "home_order": home_order,
        "home_photo_title": home_photo_title,
    }
    return render(requests, 'index.html', ctx)


def allproducts(requests):
    home_order = Orders.objects.all()

    ctx = {
        "home_order": home_order,
    }
    return render(requests, 'all-products.html', ctx)


def zakaz(requests):
    return render(requests, 'zakaz.html', {})


def contacts(requests):
    return render(requests, 'contacts.html', {})
