from django import forms
from .models import Item


class ItemForm(forms.ModelForm):


class Meta:
    model = Item
    fields = ['name', 'done']

# Fortsätt på Hello Django  Modifying Data  Forms
