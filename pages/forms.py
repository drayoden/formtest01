from django import forms

class HomeForm(forms.Form):
    name = forms.CharField(required=True)
    email = forms.CharField()
    msg = forms.CharField()
