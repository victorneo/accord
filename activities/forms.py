from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import EMPTY_VALUES
from .models import ActivityType


class ActivityTypeAdminForm(forms.ModelForm):
    class Meta:
        model = ActivityType
        exclude = []

    def clean(self, *args, **kwargs):
        super(ActivityTypeAdminForm, self).clean(*args, **kwargs)
        print(self.cleaned_data)

        if self.cleaned_data['reminder_weekly'] and self.cleaned_data['reminder_weekly_channel'] is None:
            self.add_error('reminder_weekly_channel', 'Weekly reminder channel needed')

        if self.cleaned_data['reminder_same_day'] and self.cleaned_data['reminder_same_day_channel'] is None:
            self.add_error('reminder_same_day_channel', 'Same day reminder channel needed')

        return self.cleaned_data
