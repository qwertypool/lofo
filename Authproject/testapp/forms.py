from django import forms
from django.contrib.auth.models import User 
from testapp.models import Adhar,VoterId,Pan,Passport,Atm,Fadhar
class SignUpForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','password','email','first_name','last_name']

class adharForm(forms.ModelForm):
    class Meta:
        model=Adhar
        fields='__all__'

class voterForm(forms.ModelForm):
    class Meta:
        model=VoterId
        fields='__all__'

class passportForm(forms.ModelForm):
    class Meta:
        model=Passport
        fields='__all__'

class panForm(forms.ModelForm):
    class Meta:
        model=Pan
        fields='__all__'

class atmForm(forms.ModelForm):
    class Meta:
        model=Atm 
        fields='__all__'

class FadharForm(forms.ModelForm):
    class Meta:
        model=Fadhar
        fields='__all__'

