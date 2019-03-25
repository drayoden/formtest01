from django import forms
from pages.models import Contact

# NOTE: chased tail for a day tracking down why 'form.is_valid() was
# failing in views.py... I had originally used the same model field;
# "TextFiled" in the form (below). A ModelForm uses a "CharField".

class HomeForm(forms.ModelForm):
    name = forms.CharField()
    email = forms.CharField()
    msg = forms.CharField()

    class Meta:
        model = Contact
        fields = ('name','email','msg',)
