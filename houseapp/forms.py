from django import forms
from .models import House


<<<<<<< Updated upstream
class HouseRegisterForm(forms.ModelForm):
=======
class HouseRegisterForm(ModelForm):
>>>>>>> Stashed changes
    class Meta:
        model = House
        fields = ['name', 'address']
