from django.urls import path
from .views import (
    HomeView,
    )

app_name = 'base_app'

urlpatterns = [
     path('', HomeView.as_view(), name='item-list'),
]