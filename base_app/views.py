from django.shortcuts import render, get_object_or_404
from .models import Item
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Item, Profile
from the_barter_app.forms import UserForm, ProfileForm
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import ListView, DetailView, View, CreateView, TemplateView
from django.db.models import Q
from django.contrib import messages
from django.shortcuts import redirect
from .forms import*
from django.utils.translation import gettext as _
from django.contrib.auth.models import User



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

        item_form = NewItemForm(request.POST, request.FILES)
        #item_form.user = Item.user

        if item_form.is_valid():

            item = item_form.save(commit=False)
            item.user = request.user
            item.save()
            messages.success(request, _('You have sucessfully added a new Item to your inventory'))
            return redirect('base_app:inventory')
        else:
            messages.error(request, item_form.errors)

    else:
        item_form = NewItemForm()
    context = {
            'i_form': item_form
    }

    return render(request, "new-item.html", context)

@login_required
def delete_item(request, slug):
    item = get_object_or_404(Item, slug=slug)
    
    if item.user == request.user:   
        item.delete()
        messages.info(request, "This item was deleted")
        return redirect("base_app:inventory")
   
#for a 100 contributions in 2020!
##################################################################################################################################
# import allauth.app_settings

# def ProfileDetail(request):
#     profile = Profile.objects.get()
#     return render(request, 'Profile.html', {'profile': profile})


@login_required
@transaction.atomic
def profileView(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, _('Your profile was successfully updated!'))
            return redirect('base_app:profile')
        else:
            messages.error(request, _('Please correct the error below.'))
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'Profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })


# def update_profile(request, user_id):
#     user = User.objects.get(pk=user_id)
#     user.profile.address = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit...'
#     user.save()
# def update_profile(request, user_id):
#     user = allauth.app_settings.USER_MODEL.objects.get(pk=user_id)
#     user.profile.address = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit...'
#     user.save()
