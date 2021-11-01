from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.Posting)
class PostingAdmin(admin.ModelAdmin):
    pass
