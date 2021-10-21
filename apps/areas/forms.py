from django import forms
from apps.areas.models import Area

class AreasForm(forms.Form):
    nombre = forms.CharField( max_length = 255, required=False)
