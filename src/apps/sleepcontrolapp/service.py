from apps.sleepcontrolapp.models import SleepPoint


def get_events():
    data_from_db = SleepPoint.objects.order_by("date", "time")
    return data_from_db


def events_exists(event: str, date: str, time: str) -> bool:
    is_exist = SleepPoint.objects.filter(
        event=event,
        date=date,
        time=time,
    ).exists()
    return is_exist


def create_event(event: str, date: str, time: str) -> None:
    SleepPoint.objects.create(event=event, date=date, time=time)


def delete_event(pk: int) -> None:
    SleepPoint.objects.get(pk=pk).delete()
