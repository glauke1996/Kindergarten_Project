from django.db import models
from django.db.models.deletion import CASCADE
from core import models as core_model


# Create your models here.


class Room(core_model.AbstractTimeStampedModel):
    INTEGER_CHOICES = (
        (1, 1),
        (2, 2),
        (3, 3),
    )

    name = models.CharField(
        max_length=30,
    )
    description = models.TextField()
    teachers = models.ForeignKey(
        "users.User", related_name="room", on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name


class Photo(core_model.AbstractTimeStampedModel):
    caption = models.CharField(
        max_length=80,
    )
    file = models.ImageField(upload_to="room_photos")
    room = models.ForeignKey("Room", related_name="photo", on_delete=models.CASCADE)

    def __str__(self):
        return self.caption
