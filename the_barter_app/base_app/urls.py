from django.urls import path
from .views import (
    HomeView,
    ShopGridView,
    InventoryView,
    ContactView,
    searchResult,
    profileView
    )

app_name = 'base_app'

urlpatterns = [
     path('', HomeView.as_view(), name='item-list'),
     path('profile/',profileView,name='profile'),
     path('shop-grid/', ShopGridView.as_view(), name='shop-grid'),
     path('my-inventory/', InventoryView.as_view(), name='inventory'),
     path('contact-us/', ContactView.as_view(), name='contact-us'),
     path('search-results/', searchResult, name='search-results'),
]
