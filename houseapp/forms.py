from django import forms
from .models import House


class HouseRegisterForm(forms.ModelForm):
    class _Meta:
        model = House
        fields = ['name', 'address']
