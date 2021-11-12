from django import forms
from django.forms import fields, widgets
from . import models


class CreatePhotoForm(forms.ModelForm):
    class Meta:
        model = models.Photo
        fields = (
            "file",
            "caption",
        )
        labels = {
            "caption": "",
            "file": "",
        }
        widgets = {"caption": forms.Textarea(attrs={"placeholder": "사진 설명"})}
