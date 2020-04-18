from django import forms
from django.forms import ModelForm
from testapp.models import Myself,Enemies,Demo

class MyselfForm(forms.ModelForm):
    """Form definition for Myself."""

    class Meta:
        """Meta definition for Myselfform."""

        model = Myself
        fields = '__all__'

class EnemiesForm(forms.ModelForm):
    class Meta:
        model=Enemies
        fields='__all__'

class DemoForm(forms.ModelForm):
    class Meta:
        model=Demo
        fields='__all__'