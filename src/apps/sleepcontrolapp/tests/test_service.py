import datetime

from apps.sleepcontrolapp.service import (
    create_event,
    delete_event,
    event_exists,
)
from django.test import TestCase

from apps.sleepcontrolapp.models import SleepPoint


class CreateEventTest(TestCase):
    def test_event_created(self):
        event = "UP"
        date = datetime.date(2020, 8, 10)
        time = datetime.time(20, 12)
        obj = create_event(event=event, date=date, time=time)
        same_obj = SleepPoint.objects.get(pk=obj.pk)
        self.assertEqual(obj, same_obj)

    def test_events_attributes(self):
        event = "UP"
        date = datetime.date(2020, 8, 10)
        time = datetime.time(20, 12)
        obj = create_event(event=event, date=date, time=time)
        same_obj = SleepPoint.objects.get(pk=obj.pk)
        self.assertEqual(same_obj.event, event)
        self.assertEqual(same_obj.date, date)
        self.assertEqual(same_obj.time, time)

    def test_return_type(self):
        event = "UP"
        date = datetime.date(2020, 8, 10)
        time = datetime.time(20, 12)
        obj = create_event(event=event, date=date, time=time)
        self.assertIsInstance(obj, SleepPoint)

    def test_return_object_attributes(self):
        event = "UP"
        date = datetime.date(2020, 8, 10)
        time = datetime.time(20, 12)
        obj = create_event(event=event, date=date, time=time)
        self.assertEqual(obj.event, event)
        self.assertEqual(obj.date, date)
        self.assertEqual(obj.time, time)


class ExistsTest(TestCase):
    def test_exists(self):
        event = "UP"
        date = datetime.date(2023, 2, 21)
        time = datetime.time(8, 20)
        SleepPoint.objects.create(event=event, date=date, time=time)
        is_exist = event_exists(event=event, date=date, time=time)
        self.assertTrue(is_exist)

    def test_not_exists(self):
        event = "UP"
        date = datetime.date(2020, 2, 21)
        time = datetime.time(8, 20)
        is_exist = event_exists(event=event, date=date, time=time)
        self.assertFalse(is_exist)


class DeleteTest(TestCase):
    def test_delete(self):
        event = "UP"
        date = datetime.date(2020, 8, 10)
        time = datetime.time(20, 12)
        obj = create_event(event=event, date=date, time=time)
        delete_event(obj.pk)
        empty = SleepPoint.objects.filter(pk=obj.pk)
        self.assertEqual(list(empty), [])
