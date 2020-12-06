from django.shortcuts import render
from .models import Item
from django.views.generic import ListView, DetailView, View, CreateView, TemplateView

#CLASS BASED VIEWS
class HomeView(ListView):
   model = Item
   template_name = "index.html"

context = {
    'items': Item.objects.all()
}

def item_list(request):
    return render(request, "index.html", context)

class ShopGridView(TemplateView):
    template_name = "shop-grid.html"

class InventoryView(TemplateView):
    template_name = "inventory.html"

class ContactView(TemplateView):
    template_name = "contact.html"

#FUNCTION BASED VIEWS





    