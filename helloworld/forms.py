from django import forms

class HelloForm(forms.Form):
    name = forms.CharField(max_length=100)
