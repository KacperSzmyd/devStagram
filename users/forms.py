from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


class UserSignupForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'email', 'password1', 'password2']
        help_texts = {
            'username': None,
            'first_name': None,
            'email': None,
            'password1': None,
            'password2': None
        }

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['first_name'].required = False

