from django.db import models

# NOTE: chased tail for a day tracking down why 'form.is_valid() was
# failing in views.py... I had originally used the same model field;
# "TextFiled" in forms.py. A ModelForm uses a "CharField". 

class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=150)
    msg = models.TextField()
    date = models.DateTimeField(auto_now=True)
