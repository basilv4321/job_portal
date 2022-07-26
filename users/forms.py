from django import forms
from django.contrib.auth.forms import UserCreationForm
from users.models import User


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model=User
        fields=[
            'first_name',
            'username',
            'email',
            'phone',
            'role',
            'password1',
            'password2'
        ]

class SigninForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput())




