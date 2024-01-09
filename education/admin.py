from django.contrib import admin

from education.models import Module


@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'owner',)
    