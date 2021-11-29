from django import forms
from apps.empleados.models import Empleado

class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = ['user', 'area']
        widgets = {
            "user": forms.Select(attrs={'class': 'form-control form-control-alternative', 'placeholder': 'Usuario'}),
            "area": forms.Select(attrs={'class': 'form-control form-control-alternative', 'placeholder': 'Area'})
        }
