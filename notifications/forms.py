from django import forms
from . import models


class CreatePhotoForm(forms.ModelForm):
    class Meta:
        model = models.Photo
        fields = (
            "file",
            "caption",
        )
        labels = {
            "file": "",
            "caption": "",
        }
        widgets = {
            "caption": forms.Textarea(attrs={"placeholder": "사진 설명", "class": "w-100"}),
        }

    def save(self, pk, *args, **kwargs):
        photo = super().save(commit=False)
        post = models.Posting.objects.get(pk=pk)
        photo.post = post
        photo.save()


class CreatePostForm(forms.ModelForm):
    class Meta:
        model = models.Posting
        fields = (
            "title",
            "content",
        )
        labels = {
            "title": "",
            "content": "",
        }
        widgets = {
            "title": forms.TextInput(
                attrs={"placeholder": "제목", "class": "w-100 rounded"}
            ),
            "content": forms.Textarea(
                attrs={"placeholder": "내용", "class": "w-100 rounded"}
            ),
        }
