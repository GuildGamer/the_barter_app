from django.shortcuts import render
from .models import Item
from django.views.generic import ListView, DetailView, View, CreateView

#CLASS BASED VIEWS
class HomeView(ListView):
   model = Item
   template_name = "index.html"

context = {
    'items': Item.objects.all()
}

class ShopGridView(ListView):
   model = Item
   template_name = "shop-grid.html"

#FUNCTION BASED VIEWS
def item_list(request):
    return render(request, "index.html", context)


    