from django.db import models
from django.urls import reverse
from core.models import AbstractTimeStampedModel


# Create your models here.


class Posting(AbstractTimeStampedModel):
    title = models.CharField(max_length=80)
    content = models.TextField()
    picture = models.ImageField()
    user = models.ForeignKey(
        "users.User", related_name="posting", on_delete=models.CASCADE
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("notifications:detail", kwargs={"pk": self.pk})
