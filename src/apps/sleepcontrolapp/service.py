from datetime import datetime

from apps.sleepcontrolapp.models import SleepPoint
from django.db.models.query import QuerySet


def get_events() -> QuerySet[SleepPoint]:
    queryset = SleepPoint.objects.all().order_by("date", "time")
    return queryset


def events_exists(
    event: str, date: datetime.date, time: datetime.time
) -> bool:
    is_exist = SleepPoint.objects.filter(
        event=event,
        date=date,
        time=time,
    ).exists()
    return is_exist


def create_event(
    event: str, date: datetime.date, time: datetime.time
) -> SleepPoint:
    event = SleepPoint.objects.create(event=event, date=date, time=time)
    return event


def delete_event(pk: int) -> None:
    SleepPoint.objects.filter(pk=pk).delete()
