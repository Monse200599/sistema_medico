from django import forms
from apps.puestos.models import Puesto


class PuestoForm(forms.ModelForm):
    class Meta:
        model = Puesto
        fields = ['nombre']
        widgets = {
            "nombre": forms.TextInput(attrs={'class': 'form-control form-control-alternative', 'placeholder': 'Nombre del puesto'})
        }
