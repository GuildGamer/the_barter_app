from django import forms
from base_app.models import Item, RequestsToMe
from django.contrib.auth.models import User


class NewItemForm(forms.ModelForm):
    class Meta():
        model = Item
        fields = ('title', 'estimated_value', 'category', 'condition', 'slug', 'description', 'image', 'image_1', 'image_2', 'image_3')

class RequestsForm(forms.ModelForm):
    class Meta():
        model = RequestsToMe
        fields = ('quantity',)
"""
        widgets = {
        'title' : forms.TextInput(attrs={'placeholder':'Title*'}),
        'estimated_value' : forms.NumberInput(attrs={'placeholder':'Estimated Value'}),
        'category' : forms.TextInput(attrs={'placeholder':'Category*'}),
        'condition' : forms.TextInput(attrs={'placeholder':'Item Condition*'}),
        'slug' : forms.TextInput(attrs={'placeholder': 'Unique ID*'}),
        'description' : forms.TextInput(attrs={'placeholder': 'Description*'}),
        'image' : forms.FileInput(attrs={'placeholder': 'First Image*'}),
        'image_1' : forms.FileInput(attrs={'placeholder': 'Second Image*'}),
        'image_2' : forms.FileInput(attrs={'placeholder': 'Third Image'}),
        'image_3' : forms.FileInput(attrs={'placeholder': 'Fourth Image'}),
    }

"""