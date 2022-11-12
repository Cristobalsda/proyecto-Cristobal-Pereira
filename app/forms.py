from django import forms
from app.models import Socio

class FormProyecto(forms.ModelForm):
    class Meta:
        model = Socio
        fields = '__all__'