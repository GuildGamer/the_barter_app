from allauth.account.forms import SignupForm, LoginForm
from django import forms
from base_app.models import Profile
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column
from django.contrib.auth.models import User
from django.core.files.images import get_image_dimensions


class CustomSignupForm(SignupForm):
    first_name = forms.CharField(max_length=30, label='First Name')
    last_name = forms.CharField(max_length=30, label='Last Name')
    def signup(self, request, user):
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()
        return user

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('phone_1', 'phone_2', 'address', 'city', 'state', 'gender', 'profile_pic')

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-group'

    def clean_profile_pic(self):
                profile_pic = self.cleaned_data['profile_pic']

                try:
                    w, h = get_image_dimensions(profile_pic)

                    #validate dimensions
                    max_width = max_height = 300
                    if w > max_width or h > max_height:
                        raise forms.ValidationError(
                            u'Please use an image that is '
                             '%s x %s pixels or smaller.' % (max_width, max_height))

                    #validate content type
                    main, sub = profile_pic.content_type.split('/')
                    if not (main == 'image' and sub in ['jpeg', 'pjpeg', 'png']):
                        raise forms.ValidationError(u'Please use a JPEG, or PNG image.')

                    #validate file size
                    # if len(profile_pic) > (20 * 1024):
                    #     raise forms.ValidationError(
                    #         u'Avatar file size may not exceed 20k.')

                except AttributeError:
                    """
                    Handles case when we are updating the user profile
                    and do not supply a new Profile picture
                    """
                    pass

                return profile_pic
