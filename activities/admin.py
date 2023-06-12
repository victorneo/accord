from django.contrib import admin
from .forms import ActivityTypeAdminForm
from .models import ActivityType, Activity


class ActivityTypeAdmin(admin.ModelAdmin):
    form = ActivityTypeAdminForm


class ActivityAdmin(admin.ModelAdmin):
    pass


admin.site.register(ActivityType, ActivityTypeAdmin)
admin.site.register(Activity, ActivityAdmin)
