from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):
    pass
