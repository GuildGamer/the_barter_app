from django import forms
from base_app.models import Item
from django.contrib.auth.models import User


class NewItemForm(forms.ModelForm):
    class Meta():
        model = Item
        fields = ('title', 'estimated_value', 'category', 'condition', 'slug', 'description', 'image', 'image_1', 'image_2', 'image_3', 'user')