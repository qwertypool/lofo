from django import forms

class StudentRegister(forms.Form):
    Name=forms.CharField();
    Roll=forms.IntegerField();