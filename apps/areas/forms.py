from django import forms
from apps.areas.models import Area

class AreasForm(forms.ModelForm):
    class Meta:
        model = Area
        fields = ['nombre']
        widgets = {
            "nombre": forms.TextInput(attrs={'class': 'form-control form-control-alternative', 'placeholder': 'Nombre del área'})
        }
