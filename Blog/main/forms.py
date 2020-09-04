from django import forms
from .models import Comments


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = [
            'Name',
            'comment'
        ]
        widgets = {
            'Name':forms.TextInput(attrs={'class': 'form-control','placeholder': 'Type your name','id': 'username'}),
            'comment': forms.Textarea(attrs={'class': 'form-control','placeholder': 'Type your comment','id': 'usercomment','rows': '4'})
        }
        labels = None