from django import forms
from .models import House
from django.forms import ModelForm

PROVINCES= [
    ('on', 'Ontario'),
    ('ab', 'Alberta'),
    ('bc', 'British Columbia'),
    ('mb', 'Manitoba'),
    ('nb', 'New Brunswick'),
    ('nl', 'Newfoundland and Labrador'),
    ('nt', 'Northwest Territories'),
    ('ns', 'Nova Scotia'),
    ('nu', 'Nunavut'),
    ('pe', 'Prince Edward Island'),
    ('qc', 'Quebec'),
    ('sk', 'Saskatchewan'),
    ('yk', 'Yukon'),
    ]
class HouseRegisterForm(ModelForm, request):
    house_name = forms.CharField(max_length=30, required=True)
    house_address = forms.CharField(max_length=30, required=True)
    house_province = forms.CharField(label='Province?', widget=forms.Select(choices=PROVINCES))
    house_postcode = forms.CharField(max_length=7, required=True)

    class Meta:
        model = House
        fields = ['house_name', 'house_address', 'house_province', 'house_postcode']
