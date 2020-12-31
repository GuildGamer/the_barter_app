from allauth.account.forms import SignupForm, LoginForm
from django import forms
from base_app.models import Profile
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column
from django.contrib.auth.models import User

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

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.helper = FormHelper()
    #     self.helper.layout = Layout(
    #         Row(
    #             Column('first_name', css_class='form-group col-md-6 mb-0'),
    #             Column('last_name', css_class='form-group col-md-6 mb-0'),
    #             css_class='form-row'
    #         ),
    #         'email'
    #         )

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('phone_1', 'phone_2', 'address', 'city', 'state', 'gender')

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-group'
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.helper = FormHelper()
    #     self.helper.layout = Layout(
    #         Row(
    #             Column('phone_1', css_class='form-group col-md-6 mb-0'),
    #             Column('phone_2', css_class='form-group col-md-6 mb-0'),
    #             css_class='form-row'
    #         ),
    #         'address',
    #         Row(
    #             Column('city', css_class='form-group col-md-6 mb-0'),
    #             Column('state', css_class='form-group col-md-6 mb-0'),
    #             css_class='form-row'
    #         ),
    #         'gender',
    #         # Submit('submit', 'Sign in')
    #     )
