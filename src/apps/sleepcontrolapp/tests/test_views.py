import datetime
from unittest.mock import patch

from django.test import TestCase
from django.urls import reverse


class SleepControlTest(TestCase):
    @patch("apps.sleepcontrolapp.service.get_events")
    def test_get(self, get_events_mock):
        response = self.client.get(reverse("main"))
        get_events_mock.assert_called_once_with()
        self.assertEqual(response.status_code, 200)

    @patch("apps.sleepcontrolapp.service.create_event")
    def test_add(self, create_event_mock):
        data = {"event": "DOWN", "date": "2023-02-21", "time": "23:41"}
        response = self.client.post(reverse("add"), data=data)
        create_event_mock.assert_called_once_with(
            event="DOWN",
            date=datetime.date(2023, 2, 21),
            time=datetime.time(23, 41),
        )
        self.assertEqual(response.status_code, 302)

    @patch("apps.sleepcontrolapp.service.delete_event")
    def test_delete(self, delete_event_mock):
        pk = {"pk": 100}
        response = self.client.post(reverse("delete"), data=pk)
        delete_event_mock.assert_called_once_with(pk=100)
        self.assertEqual(response.status_code, 302)
