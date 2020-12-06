from django.urls import path
from .views import (
    HomeView,
    ShopGridView,
    )

app_name = 'base_app'

urlpatterns = [
     path('', HomeView.as_view(), name='item-list'),
     path('shop-grid/', ShopGridView.as_view(), name='shop-grid'),
]