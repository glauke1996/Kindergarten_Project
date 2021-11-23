from django import forms
from django.db.models import fields
from django.forms import widgets
from . import models
from mptt.forms import TreeNodeChoiceField


class CreateCommentForm(forms.ModelForm):
    parent = TreeNodeChoiceField(queryset=models.Comment.objects.all())

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["parent"].widget.attrs.update({"class": "d-none"})
        self.fields["parent"].label = ""
        self.fields["parent"].required = False

    class Meta:
        model = models.Comment
        fields = (
            "parent",
            "content",
        )
        labels = {
            "content": "",
        }
        widgets = {
            "content": forms.Textarea(
                attrs={"class": "form-control kagenoaru-box", "rows": "5"}
            )
        }

    def save(self, *args, **kwargs):
        # content = super().save(commit=False)
        # return content
        models.Comment.objects.rebuild()  ##뭐임 이거
        return super(CreateCommentForm, self).save(*args, **kwargs)
