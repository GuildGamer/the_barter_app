from django.db import models
from django.conf import settings
from django.shortcuts import reverse
import allauth.app_settings
from allauth.utils import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User


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
    slug = models.SlugField(unique=True)
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
    def set_sort_by_condition(self):
        return Item.objects.order_by('condition').all()
    def set_sort_by_date(self):
        return Item.objects.order_by('-date_uploaded').all()
    def get_absolute_url(self):
        return reverse('base_app:item-details', kwargs={'slug': self.slug})
class TradeItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='suitor', on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE, blank=True, null=True)
    quantity = models.IntegerField(default=1) 
    request_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    response_date = models.DateTimeField(blank=True, null=True)
    responded = models.BooleanField(default=False)


    def __str__(self):
        return self.item.title


'''class Requests(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    items = models.ManyToManyField(TradeItem)
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username'''

class RequestsToMe(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='item_owner', on_delete=models.CASCADE)
    suitor = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='request_maker', on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE, blank=True, null=True)
    quantity = models.IntegerField(default=1, blank=True, null=True) 

    def __str__(self):
        return self.suitor.username

  

class Inventory(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.user.username


#######################################################################################################################
GENDERS =(('M', 'MALE'),
            ('F', 'FEMALE'))


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15, blank=True)
    address = models.CharField(max_length=200, blank=True)
    gender = models.CharField(choices=GENDERS, max_length=20, blank=True) #, input_formats=settings.DATE_INPUT_FORMATS)
    phone_1 = models.CharField(max_length=15, blank=True)
    phone_2 = models.CharField(max_length=15, blank=True)
    address = models.CharField(max_length=200, blank=True)
    city = models.CharField(blank=True, max_length=100)
    state = models.CharField(blank=True, max_length=100)
    profile_pic = models.ImageField(upload_to='profile_pics', default='profile_pics/default.png')

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
