from django import forms
from . import models
from users import models as user_model


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

    def save(self, pk, bool, *args, **kwargs):
        post = super().save(commit=False)
        user = user_model.User.objects.get(pk=pk)
        post.user = user
        if bool:
            post.notification = True
        post.save()
