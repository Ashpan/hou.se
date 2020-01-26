from django import forms
from .models import House
from django.forms import ModelForm


class HouseRegisterForm(ModelForm):
    class _Meta:
        model = House
        fields = ['name', 'address']
