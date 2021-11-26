from abc import abstractclassmethod
from django.db import models
from django.db.models.fields import CharField
from core.models import AbstractTimeStampedModel
from mptt.models import MPTTModel, TreeForeignKey

# Create your models here.


class Review(AbstractTimeStampedModel):
    review = models.TextField()
    user = models.ForeignKey(
        "users.User", related_name="reviews", on_delete=models.CASCADE
    )
    post = models.ForeignKey(
        "notifications.Posting", related_name="reviews", on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.user}'s comment"

    class Meta:
        ordering = ("-created",)


class Comment(MPTTModel):
    post = models.ForeignKey(
        "notifications.Posting", related_name="comments", on_delete=models.CASCADE
    )
    content = models.TextField()
    parent = TreeForeignKey(
        "self", related_name="children", on_delete=models.CASCADE, null=True, blank=True
    )
    user = models.ForeignKey(
        "users.User", related_name="users", on_delete=models.CASCADE
    )
    publish = models.DateTimeField(auto_now_add=True)

    class MPTTMeta:
        order_insertion_by = ["publish"]

    def __str__(self):
        return f"{self.user}'s comment"
