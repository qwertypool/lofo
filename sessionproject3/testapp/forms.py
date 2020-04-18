from django import forms

class AddItemForm(forms.Form):
    name = forms.CharField(max_length = 150)
    quantity = forms.IntegerField()
    
    
