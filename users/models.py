from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse

# Create your models here.
class User(AbstractUser):

    GENDER_CHOICES = (
        ("male", "Male"),
        ("femail", "femail"),
        ("other", "Other"),
    )

    avatar = models.ImageField(upload_to="avatars", null=True, blank=True)
    bio = models.TextField(default="", blank=True)
    gender = models.CharField(
        choices=GENDER_CHOICES,
        max_length=10,
        default="",
    )
    birth = models.DateField(null=True)

    def get_absolute_url(self):
        return reverse("users:profile", kwargs={"pk": self.pk})
