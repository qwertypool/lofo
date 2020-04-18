from django import forms
from django.core import validators

def starts_with(value):
    if value[0]!='d':
        raise forms.ValidationError('name should start with d')

def clean(self):
      print('Total Form Validation by using single clean method...') 
      total_cleaned_data=super(FeedbackForm,self).clean() 
      inputpass=total_cleaned_data.get("password") 
      inputrpass=total_cleaned_data.get("repassword")
      if inputpass!=inputrpass: 
        raise forms.ValidationError("Passwords did not match!")
    
def bot(value):
    if len(value)>0:
        raise forms.ValidationError('U R A FUCKING ROBO !!!!!')


class FeedbackForm(forms.Form):
    Name=forms.CharField()
    rollno=forms.IntegerField()
    email=forms.EmailField()
    password=forms.CharField(widget=forms.PasswordInput)
    repassword=forms.CharField(label='password(again)',widget=forms.PasswordInput)
    feedback=forms.CharField(widget=forms.Textarea,validators=[validators.MaxLengthValidator(40),validators.MinLengthValidator(5)])
    bot_handler=forms.CharField(required=False,widget=forms.HiddenInput,validators=[bot])



