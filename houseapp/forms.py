from django import forms
from .models import House


class HouseRegisterForm(forms.ModelForm):
    class Meta:
        model = House
        fields = ['name', 'address']
