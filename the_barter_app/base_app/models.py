from django.db import models
from django.conf import settings
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
    slug = models.SlugField()
    description = models.TextField(max_length=400)
    condition = models.CharField(choices=CONDITION_CHOICES, max_length=1)
    image = models.ImageField()
    image_1 = models.ImageField()
    image_2 = models.ImageField(blank=True, null=True)
    image_3 = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.title

class TradeItem(models.Model):

    pass
class Inventory(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    item = models.ForeignKey(Item, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.user.username


#######################################################################################################################
GENDERS =(('M', 'MALE'),
            ('F', 'FEMALE'))
#
# # User = allauth.app_settings.USER_MODEL
# class Profile(models.Model):
#     user = models.ForeignKey(allauth.app_settings.USER_MODEL, on_delete=models.CASCADE)
#     address = models.CharField(max_length=30, blank=True)
#     birth_date = models.DateField(null=True, blank=True)
#     gender = models.CharField(max_length=1, choices=GENDERS)
#
# # def __str__(self):
# #     return self.user.first_name
#
#
# @receiver(post_save, sender=allauth.app_settings.USER_MODEL)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)
#
# @receiver(post_save, sender=allauth.app_settings.USER_MODEL)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()




class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15, blank=True)
    address = models.CharField(max_length=200, blank=True)
    gender = models.CharField(choices=GENDERS, max_length=20, blank=True) #, input_formats=settings.DATE_INPUT_FORMATS)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
