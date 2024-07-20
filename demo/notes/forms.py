from django import forms
from .models import Note

class CreateForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'content']
