from django import forms
from users.models import *


class ContactForm(forms.ModelForm):
    
    class Meta:
        model = ContactUs
        fields = "__all__"