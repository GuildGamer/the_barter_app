from django.db import models
from django.conf import settings
from django.shortcuts import reverse

CATEGORY_CHOICES = (
    ('CL', 'Clothing'),
    ('ED', 'Electronics & Devices'),
    ('KD', 'Kids'),
    ('FI', 'Food Items'),
    ('KI', 'Kitchen'),
    ('FH', 'Furniture & Housing'),
)

CONDITION_CHOICES = (
    ('N', 'New'),
    ('U', 'Used'),
)

class Item(models.Model):
    title = models.CharField(max_length=100)
    estimated_value = models.FloatField(blank=True, null=True)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    slug = models.SlugField()
    description = models.TextField(max_length=400)
    condition = models.CharField(choices=CONDITION_CHOICES, max_length=1)
    image = models.ImageField()
    image_1 = models.ImageField()
    image_2 = models.ImageField(blank=True, null=True)
    image_3 = models.ImageField(blank=True, null=True)
    date_uploaded = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    

    def __str__(self):
        return self.title
    def set_sortBy_Date_Uploaded(self):
        Item.objects.order_by('date_uploaded')
    def set_sortBy_Item_Condition(self):
        Item.objects.order_by('condition')
    def get_absolute_url(self):
        return reverse('base_app:item-details', kwargs={'slug': self.slug})
class TradeItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE, blank=True, null=True)
    request_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    response_date = models.DateTimeField(blank=True, null=True)
    accepted = models.BooleanField(default=False, blank=True, null=True)


    def __str__(self):
        return self.title

class Inventory(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.user.username