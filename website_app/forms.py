from django import forms
from .models import Register
class Register_form(forms.ModelForm):
    class Meta:
        model=Register
        fields='__all__'
