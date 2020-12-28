from django.urls import path
from django.conf.urls import url

from .views import (
    HomeView,
    ShopGridView,
    InventoryView,
    ContactView,
    searchResult,
    ProfileDetail, EditProfile
    )

app_name = 'base_app'

urlpatterns = [
     path('', HomeView.as_view(), name='item-list'),
     # path('profile/',profileView,name='profile'),
     path('shop-grid/', ShopGridView.as_view(), name='shop-grid'),
     path('my-inventory/', InventoryView.as_view(), name='inventory'),
     path('contact-us/', ContactView.as_view(), name='contact-us'),
     path('search-results/', searchResult, name='search-results'),
     path('profile/', ProfileDetail, name='ProfileDetail'),
     path('profile/edit/', EditProfile, name='EditProfile')
     # url(r'^Profile/(?P<slug>[-\w]+)/$', ProfileDetail, name='ProfileDetail'),
     # url(r'^Profile/(?P<slug>[-\w]+)/edit/$', EditProfile, name='EditProfile'),
]
