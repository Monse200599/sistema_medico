from django import forms
from django.forms import widgets
from .models import Bienes

class BienesForm(forms.ModelForm):
    class Meta:
        model = Bienes
        fields = [
            'tipo',
            'num_unidades',
            'num_cajas',
            'lote',
            'caducidad',
            'tipo_bienes'
        ]
        widgets = {
            "tipo": forms.TextInput(attrs={'class': 'form-control form-control-alternative', 'placeholder': 'Nombre del bien'}),
            "num_unidades": forms.NumberInput(attrs={'class': 'form-control form-control-alternative', 'placeholder': 'Número de unidades'}),
            "num_cajas": forms.NumberInput(attrs={'class': 'form-control form-control-alternative', 'placeholder': 'Número de cajas'}),
            "num_cajas":  forms.NumberInput(attrs={'class': 'form-control form-control-alternative', 'placeholder': 'Número de cajas'}),
            "lote": forms.TextInput(attrs={'class': 'form-control form-control-alternative', 'placeholder': 'Lote'}),
            "caducidad": forms.DateInput(attrs={'type':'date', 'class': 'form-control form-control-alternative datepicker', 'placeholder': 'Caducidad'}),
            "tipo_bienes": forms.Select(attrs={'class': 'form-control form-control-alternative', 'placeholder': 'Tipo bien'})
        }