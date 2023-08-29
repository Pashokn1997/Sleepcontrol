import datetime

from apps.sleepcontrolapp.service import (
    create_event,
    delete_event,
    events_exists,
)
from django.core.exceptions import ValidationError
from django.test import TestCase

from apps.sleepcontrolapp.models import SleepPoint
from django.test import Client


class SleepControlTest(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        SleepPoint.objects.create(
            event="UP", date="2023-02-21", time="08:20", pk=100
        )
        SleepPoint.objects.create(
            event="DOWN", date="2023-02-21", time="23:40", pk=101
        )

    def test_create_success(self):
        event = "UP"
        date = datetime.date(2020, 8, 10)
        time = datetime.time(20, 12)
        obj = create_event(event=event, date=date, time=time)
        self.assertEqual(obj.pk, 1)

    def test_create_invalid_date(self):
        event = "UP"
        date = "2020-8-40"
        time = datetime.time(20, 12)
        with self.assertRaises(ValidationError):
            create_event(event=event, date=date, time=time)

    def test_create_invalid_time(self):
        event = "UP"
        date = datetime.date(2020, 8, 10)
        time = "31:09"
        with self.assertRaises(ValidationError):
            create_event(event=event, date=date, time=time)

    def test_exists(self):
        event = "UP"
        date = datetime.date(2023, 2, 21)
        time = datetime.time(8, 20)
        is_exist = events_exists(event=event, date=date, time=time)
        self.assertEqual(is_exist, True)

    def test_not_exists(self):
        event = "UP"
        date = datetime.date(2020, 2, 21)
        time = datetime.time(8, 20)
        is_exist = events_exists(event=event, date=date, time=time)
        self.assertEqual(is_exist, False)

    def test_delete(self):
        data = 100
        delete_event(data)
        obj = SleepPoint.objects.filter(pk=data)
        self.assertEqual(list(obj), [])
