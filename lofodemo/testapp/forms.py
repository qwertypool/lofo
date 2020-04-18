from django import forms
from django.forms import ModelForm
from testapp.models import Lost,Found
from django.contrib.auth.models import User
class SignUpForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','password','email','first_name','last_name']

class LostForm(forms.ModelForm):
    class Meta:
        model = Lost
        fields = '__all__'

class FoundForm(forms.ModelForm):
    class Meta:
        model = Found
        fields = '__all__'