from django.db import models
from django.urls import reverse
from django.http import Http404
from core.models import AbstractTimeStampedModel


# Create your models here.


class Posting(AbstractTimeStampedModel):
    title = models.CharField(max_length=80)
    content = models.TextField()
    # picture = models.ImageField(upload_to="pictures", null=True, blank=True)
    user = models.ForeignKey(
        "users.User", related_name="posting", on_delete=models.CASCADE
    )

    class Meta:
        ordering = ("-created",)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("notifications:detail", kwargs={"pk": self.pk})


class Photo(AbstractTimeStampedModel):
    file = models.ImageField(upload_to="post_photos")
    caption = models.CharField(max_length=80)
    post = models.ForeignKey("Posting", related_name="photos", on_delete=models.CASCADE)

    def __str__(self):
        return self.caption
