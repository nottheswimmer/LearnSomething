from django.contrib import admin

from . import models


# Register your models here.
@admin.register(models.WordAssociationSet)
class WordAssociationSetAdmin(admin.ModelAdmin):
    pass


@admin.register(models.WordAssociation)
class WordAssociation(admin.ModelAdmin):
    pass
