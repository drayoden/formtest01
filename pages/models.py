from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=150)
    msg = models.TextField()
    date = models.DateTimeField(auto_now=True)
