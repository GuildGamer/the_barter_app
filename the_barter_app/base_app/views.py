from django.shortcuts import render, get_object_or_404
from .models import Item
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, View, CreateView, TemplateView
from django.db.models import Q
from django.contrib import messages
from django.shortcuts import redirect
from .forms import*

#CLASS BASED VIEWS
class HomeView(ListView):
   model = Item
   template_name = "index.html"

context = {
    'items': Item.objects.all()
}

def item_list(request):
    return render(request, "index.html", context)

class ItemDetailView(DetailView):
    model = Item
    template_name = "product.html"

class ShopGridView(ListView):
    model = Item
    template_name = "shop-grid.html"

    def set_sortBy_date_uploaded():
        pass
    def set_sortBy_Item_Condition():
        pass

class InventoryView(ListView):
    model = Item
    template_name = "inventory.html"

class ContactView(TemplateView):
    template_name = "contact.html"

#FUNCTION BASED VIEWS

def searchResult(request):
    product = None
    object_list = None
    if 'search' in request.GET:
        product = request.GET.get('search')
        if product != '':
            try:
                object_list = Item.objects.all().filter(Q(title__icontains=product) | Q(description__icontains=product) | Q(category__icontains=product))
            except ObjectDoesNotExist:
                object_list = None
                messages.error(request, "Sorry there are no search results")
            return render(request, "search.html", {'items':object_list, 'searched_item':product})
        else:
            return redirect("base_app:item-list")
    else:
        messages.error(request, "Sorry there are no search results")
        return render(request, "search.html", {})
        
#new item view
@login_required
def new_item(request):

    if request.method == 'POST':

        item_form = NewItemForm(data=request.POST)
        #item_form.user = Item.user

        if item_form.is_valid():

            item = item_form.save()
            item.save()

        else:
            messages.error(request, item_form.errors)

    else:
        item_form = NewItemForm()
    context = {
            'i_form': item_form
    }

    return render(request, "new-item.html", context)




    