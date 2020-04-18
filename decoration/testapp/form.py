from django import forms
from testapp.models import adhar

class adharForm(forms.ModelForm):
    class Meta:
        model='adhar'
        fields='__all__'