from django.contrib import admin
from . import models as conversation_model

# Register your models here.


@admin.register(conversation_model.Message)
class MessageAdmin(admin.ModelAdmin):
    pass


@admin.register(conversation_model.Conversation)
class ConversationAdmin(admin.ModelAdmin):
    pass
