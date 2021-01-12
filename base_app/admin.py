from django.contrib import admin
from .models import Item, TradeItem, Inventory, Profile

admin.site.register(Item)
admin.site.register(TradeItem)
admin.site.register(Inventory)
admin.site.register(Profile)
