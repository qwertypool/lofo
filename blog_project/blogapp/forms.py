from django import forms
from blogapp.models import Comment

class EmailSendForm(forms.Form):
    name = forms.CharField(max_length = 150)
    emailId = forms.EmailField()
    to =forms.EmailField()
    comments = forms.CharField(required=False,widget=forms.Textarea)
    

class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=('name','email','body')
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'special'})
        self.fields['body'].widget.attrs.update(size='20')
    
    
    