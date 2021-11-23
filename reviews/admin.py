from django.contrib import admin
from . import models
from mptt.admin import MPTTModelAdmin

# Register your models here.


@admin.register(models.Review)
class ReviewAdmin(admin.ModelAdmin):
    pass


admin.site.register(models.Comment, MPTTModelAdmin)
