from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name="home"),
    path('all-products/', allproducts, name="all-products"),
    path('order/', zakaz, name="zakaz"),
    path('contact/', contacts, name="contact"),
]
