from dataclasses import field
from . import models
from django import forms
from django.forms import ModelForm

class NftInfoForm(forms.ModelForm):
    class Meta:
         model = models.NftRegistration
         fields = "__all__"