from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import BaseUserCreationForm, UserChangeForm, AuthenticationForm
from django.forms import widgets

from accounts.models import Profile

UserModel = get_user_model()

class AppUserCreationForm(BaseUserCreationForm):
    class Meta:
        model = UserModel
        fields = ('email',)

class AppUserChangeForm(UserChangeForm):
    class Meta:
        model = UserModel
        fields='__all__'


class AppLoginForm(AuthenticationForm):
    username = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                'autofocus':True
            }
        )
    )
    password = forms.CharField(
        label='Password',
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                'autocomplete':'current-password'
            }
        )
    )

class ProfileEditForm(forms.ModelForm):



    class Meta:
        model = Profile
        fields = ('first_name','last_name','date_of_birth','profile_picture')
        labels = {
            'first_name':'First Name',
            'last_name': 'Last Name',
            'date_of_birth': 'Date of birth',
            'profile_picture': 'Profile picture'
        }

        widgets = {
            'date_of_birth' : forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'})
        }