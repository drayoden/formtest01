from django import forms
from pages.models import Contact

class HomeForm(forms.ModelForm):
    name = forms.CharField()
    email = forms.CharField()
    msg = forms.CharField()

    class Meta:
        model = Contact
        fields = ('name','email','msg',)
