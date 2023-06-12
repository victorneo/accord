from django.contrib import admin
from django.db import models
from django.forms import TextInput, Textarea
from .models import Course, CourseReminder


class CourseAdmin(admin.ModelAdmin):
    pass


class CourseReminderAdmin(admin.ModelAdmin):
    list_display = ['course', 'message', 'start_time', 'published']
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'100'})},
    }


admin.site.register(Course, CourseAdmin)
admin.site.register(CourseReminder, CourseReminderAdmin)
