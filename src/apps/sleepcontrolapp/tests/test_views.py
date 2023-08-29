from unittest.mock import patch

from django.test import TestCase
from django.urls import reverse

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

    @patch("apps.sleepcontrolapp.service.get_events")
    def test_get(self, get_events_mock):
        response = self.client.get(reverse("main"))
        get_events_mock.assert_called_once()
        self.assertEqual(response.status_code, 200)

    @patch("apps.sleepcontrolapp.service.create_event")
    def test_add(self, create_event_mock):
        data = {"event": "DOWN", "date": "2023-02-21", "time": "23:41"}
        response = self.client.post(reverse("add"), data=data)
        create_event_mock.assert_called_once()
        self.assertEqual(response.status_code, 302)

    @patch("apps.sleepcontrolapp.service.delete_event")
    def test_delete(self, delete_event_mock):
        data = {"pk": 100}
        response = self.client.post(reverse("delete"), data=data)
        delete_event_mock.assert_called_once()
        self.assertEqual(response.status_code, 302)
