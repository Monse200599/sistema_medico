from django import forms
from django.forms import widgets
from .models import Bitacora


class BitacoraForm(forms.ModelForm):
    class Meta:
        model = Bitacora
        fields = [
            'cantidad',
            'empleado',
            'bienes'
        ]
        widgets = {
            "cantidad": forms.NumberInput(attrs={'class': 'form-control form-control-alternative', 'placeholder': 'Cantidad'}),
            "empleado": forms.Select(attrs={'class': 'form-control form-control-alternative', 'placeholder': 'Empleado'}),
            "bienes": forms.Select(attrs={'class': 'form-control form-control-alternative', 'placeholder': 'Bien solicitado'}),
        }
