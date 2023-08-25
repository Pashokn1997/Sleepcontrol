from rest_framework import serializers

from apps.sleepcontrolapp.models import SleepPoint


class SleepPointGetAddSerializer(serializers.ModelSerializer):
    class Meta:
        model = SleepPoint
        fields = ["event", "date", "time"]

    def validate(self, attrs):
        queryset = SleepPoint.objects.all()
        for item in queryset:
            if (
                item.event == attrs["event"]
                and item.date == attrs["date"]
                and item.time == attrs["time"]
            ):
                raise serializers.ValidationError("Обьект уже сушествует")
        return attrs
