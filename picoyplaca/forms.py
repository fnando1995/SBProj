from django import forms
from .models import Car

class CarForm(forms.ModelForm):
    """
    Model Form do obtain data for a Car Model (object)
    """
    class Meta:
        model = Car
        fields = '__all__'
        widgets = {
            'placa': forms.TextInput(attrs={'class': 'form-control'}),
            'marca': forms.TextInput(attrs={'class': 'form-control'}),
            'color': forms.TextInput(attrs={'class': 'form-control'}),
        }