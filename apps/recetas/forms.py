from django import forms
from django.forms import widgets
from .models import Receta

class RecetaForm(forms.ModelForm):
    class Meta:
        model = Receta
        fields = [
            'cantidad',
            'fecha',
            'personal',
            'bienes',
        ]
        widgets = {
            "cantidad": forms.NumberInput(attrs={'class': 'form-control form-control-alternative', 'placeholder': 'Número de unidades'}),
            "fecha": forms.DateInput(attrs={'type':'date', 'class': 'form-control form-control-alternative datepicker', 'placeholder': 'Caducidad'}),
            "personal": forms.Select(attrs={'class': 'form-control form-control-alternative', 'placeholder': 'Personal'}),
            "bienes": forms.Select(attrs={'class': 'form-control form-control-alternative', 'placeholder': 'Bien'}),
        }
