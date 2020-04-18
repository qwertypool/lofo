from django import forms

class NameForm(forms.Form):
    name = forms.CharField(max_length = 150)
    
class AgeForm(forms.Form):
    age = forms.IntegerField()
    
class GfForm(forms.Form):
    gf = forms.CharField(max_length = 150)
    