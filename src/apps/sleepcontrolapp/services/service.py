from apps.sleepcontrolapp.models import SleepPoint


def get_objects_from_db():
    data_from_db = SleepPoint.objects.order_by("date", "time")
    return data_from_db


def check_existed_data(data) -> bool:
    if SleepPoint.objects.filter(
        event=data["event"],
        date=data["date"],
        time=data["time"],
    ):
        return True


def create_new_object(event: str, date: str, time: str) -> None:
    SleepPoint.objects.create(event=event, date=date, time=time)


def delete_object(pk: int) -> None:
    object_for_delete = SleepPoint.objects.get(pk=pk)
    object_for_delete.delete()
