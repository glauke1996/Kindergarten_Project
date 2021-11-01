from abc import abstractclassmethod
from django.db import models
from core.models import AbstractTimeStampedModel

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
