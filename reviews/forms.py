from django import forms
from django.db.models import fields
from . import models


class CreateReviewForm(forms.ModelForm):
    class Meta:
        model = models.Review
        fields = ("review",)
        labels = {
            "review": "",
        }

    def save(self):
        review = super().save(commit=False)
        return review
