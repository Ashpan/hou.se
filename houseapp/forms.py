from django import forms
from django.contrib.auth.models import House


class SignUpForm(UserCreationForm):

    class Meta:
        model = House
        fields = ('username', 'first_name', 'last_name',
                  'email', 'password1', 'password2', )
