from django import forms
from django.forms import widgets


class BookForm(forms.Form):

    name = forms.CharField(max_length=300, label='Имя', required=True)

    email = forms.EmailField(max_length=300, label='Почта', required=True)

    text = forms.CharField(max_length=300, label='Текст', required=True, widget=widgets.Textarea)
