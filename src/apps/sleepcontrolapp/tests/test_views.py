from django.urls import reverse

from django.test import TestCase
from django.test import Client, RequestFactory

from apps.sleepcontrolapp.models import SleepPoint
from apps.sleepcontrolapp.views import SleepPointAdd


class SleepControlTest(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        SleepPoint.objects.create(
            event="up", date="2023-02-21", time="08:20", pk=100
        )
        SleepPoint.objects.create(
            event="down", date="2023-02-21", time="23:40", pk=101
        )

    def test_get(self):
        response = self.client.get(reverse("main"))
        self.assertEqual(response.status_code, 200)

    def test_add(self):
        data = {"event": "down", "date": "2023-02-21", "time": "23:41"}
        factory = RequestFactory()
        request = factory.post(SleepPointAdd, data=data)
        request2 = factory.post(SleepPointAdd, data=data)
        response = SleepPointAdd.post(self, request)
        response2 = SleepPointAdd.post(self, request2)
        obj = SleepPoint.objects.get(**data)
        self.assertEqual(obj.pk, 1)
        self.assertEqual(response2.status_code, 400)
        self.assertEqual(response.status_code, 302)

    def test_delete(self):
        data = {"pk": 100}
        response = self.client.post(reverse("delete"), data=data)
        obj = SleepPoint.objects.filter(pk=100)
        self.assertEqual(list(obj), [])
        self.assertEqual(response.status_code, 302)
