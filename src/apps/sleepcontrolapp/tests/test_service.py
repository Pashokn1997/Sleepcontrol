import datetime

from apps.sleepcontrolapp.service import (
    create_event,
    delete_event,
    events_exists,
)
from django.test import TestCase

from apps.sleepcontrolapp.models import SleepPoint


class CreateTest(TestCase):
    def test_create_success(self):
        event = "UP"
        date = datetime.date(2020, 8, 10)
        time = datetime.time(20, 12)
        obj = create_event(event=event, date=date, time=time)
        same_obj = SleepPoint.objects.get(pk=obj.pk)
        self.assertEqual(obj, same_obj)

    def test_create_true_parameters(self):
        event = "UP"
        date = datetime.date(2020, 8, 10)
        time = datetime.time(20, 12)
        obj = create_event(event=event, date=date, time=time)
        same_obj = SleepPoint.objects.get(pk=obj.pk)
        self.assertEqual(event, same_obj.event)
        self.assertEqual(date, same_obj.date)
        self.assertEqual(time, same_obj.time)

    def test_create_true_return_type(self):
        event = "UP"
        date = datetime.date(2020, 8, 10)
        time = datetime.time(20, 12)
        obj = create_event(event=event, date=date, time=time)
        self.assertEqual(type(obj), SleepPoint)

    def test_create_true_return_parameters(self):
        event = "UP"
        date = datetime.date(2020, 8, 10)
        time = datetime.time(20, 12)
        obj = create_event(event=event, date=date, time=time)
        self.assertEqual(event, obj.event)
        self.assertEqual(date, obj.date)
        self.assertEqual(time, obj.time)


class ExistsTest(TestCase):
    def test_exists(self):
        event = "UP"
        date = datetime.date(2023, 2, 21)
        time = datetime.time(8, 20)
        SleepPoint.objects.create(event=event, date=date, time=time)
        is_exist = events_exists(event=event, date=date, time=time)
        self.assertEqual(is_exist, True)

    def test_not_exists(self):
        event = "UP"
        date = datetime.date(2020, 2, 21)
        time = datetime.time(8, 20)
        is_exist = events_exists(event=event, date=date, time=time)
        self.assertEqual(is_exist, False)


class DeleteTest(TestCase):
    def test_delete(self):
        event = "UP"
        date = datetime.date(2020, 8, 10)
        time = datetime.time(20, 12)
        obj = create_event(event=event, date=date, time=time)
        delete_event(obj.pk)
        empty = SleepPoint.objects.filter(pk=obj.pk)
        self.assertEqual(list(empty), [])
