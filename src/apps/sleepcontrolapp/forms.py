from django.forms import ModelForm

from apps.sleepcontrolapp.models import SleepPoint


class SleepForms(ModelForm):
    class Meta:
        model = SleepPoint
        fields = ["event", "date", "time"]
