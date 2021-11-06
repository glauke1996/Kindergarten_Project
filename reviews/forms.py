from django import forms
from django.db.models import fields
from django.forms import widgets
from . import models


class CreateReviewForm(forms.ModelForm):
    class Meta:
        model = models.Review
        fields = ("review",)
        labels = {
            "review": "",
        }
        widgets = {
            "review": forms.Textarea(
                attrs={"class": "form-control kagenoaru-box", "rows": "5"}
            )
        }

    def save(self):
        review = super().save(commit=False)
        return review
