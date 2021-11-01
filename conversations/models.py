from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ForeignKey
from core import models as coremodel

# Create your models here.


class Conversation(coremodel.AbstractTimeStampedModel):

    participants = models.ManyToManyField("users.User")
    title = models.CharField(
        default="채팅방",
        max_length=20,
    )

    def __str__(self):
        return self.title


class Message(coremodel.AbstractTimeStampedModel):

    message = models.TextField()
    user = ForeignKey("users.User", on_delete=models.CASCADE)
    conversation = ForeignKey("conversations.Conversation", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} says ... {self.text}"
