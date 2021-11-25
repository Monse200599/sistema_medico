from django import forms
from django.forms import widgets
from .models import Bitacora


class BitacoraForm(forms.ModelForm):
    class Meta:
        model = Bitacora
        fields = [
            'cantidad',
            'fecha',
            'hora',
            'entrada',
            'usuario',
            'receta',
            'bienes',
            'area',
        ]
        widgets = {
            "cantidad": forms.NumberInput(attrs={'class': 'form-control form-control-alternative', 'placeholder': 'Cantidad'}),
            "fecha": forms.DateInput(attrs={'type': 'date', 'class': 'form-control form-control-alternative', 'placeholder': 'Fecha'}),
            "hora": forms.TimeInput(attrs={'type': 'time', 'class': 'form-control form-control-alternative', 'placeholder': 'Hora'}),
            "entrada":  forms.CheckboxInput(attrs={'class': 'form-control form-control-alternative', 'placeholder': 'Entrada/Salida'}),
            "usuario": forms.Select(attrs={'class': 'form-control form-control-alternative', 'placeholder': 'Usuario'}),
            "receta": forms.Select(attrs={'class': 'form-control form-control-alternative datepicker', 'placeholder': 'Receta'}),
            "bienes": forms.Select(attrs={'class': 'form-control form-control-alternative', 'placeholder': 'Bien solicitado'}),
            "area": forms.Select(attrs={'class': 'form-control form-control-alternative', 'placeholder': 'Area'}),
        }