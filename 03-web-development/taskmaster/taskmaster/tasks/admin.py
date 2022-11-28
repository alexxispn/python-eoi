from django.contrib import admin

from . import models


class TaskAdmin(admin.ModelAdmin):
    date_hierarchy = 'due_date'
    search_fields = ['name', 'due_date']
    list_filter = ['priority', 'due_date', 'finished']
    list_display = ('name', 'priority', 'due_date', 'order')


class ProjectAdmin(admin.ModelAdmin):
    pass


admin.site.register(models.Task, TaskAdmin)
admin.site.register(models.Project)
