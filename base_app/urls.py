from django.urls import path
from django.conf.urls import url

from .views import (
    HomeView,
    ShopGridView,
    InventoryView,
    ContactView,
    searchResult,
    new_item,
    ItemDetailView,
    profileView,
    delete_item,
)

app_name = 'base_app'

urlpatterns = [
     path('', HomeView.as_view(), name='item-list'),
     path('profile/',profileView,name='profile'),
     path('shop-grid/', ShopGridView.as_view(), name='shop-grid'),
     path('my-inventory/', InventoryView.as_view(), name='inventory'),
     path('contact-us/', ContactView.as_view(), name='contact-us'),
     path('search-results/', searchResult, name='search-results'),
     path('item-details/<slug>', ItemDetailView.as_view(), name='item-details'),
     path('new-item/', new_item, name='new-item'),
     path('delete-item/<slug>/',delete_item, name='delete-item'),
     # url(r'^Profile/(?P<slug>[-\w]+)/$', ProfileDetail, name='ProfileDetail'),
     # url(r'^Profile/(?P<slug>[-\w]+)/edit/$', EditProfile, name='EditProfile'),
]
