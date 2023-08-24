from django.urls import reverse


from django.test import Client, TestCase

from apps.sleepcontrolapp.models import SleepPoint


class SleepControlTest(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        SleepPoint.objects.create(event="UP", date="2023-02-21", time="08:20", pk=100)
        SleepPoint.objects.create(event="DOWN", date="2023-02-21", time="23:40", pk=101)

    def test_get(self):
        response = self.client.get(reverse("main"))
        self.assertEqual(response.status_code, 200)

    def test_add(self):
        data = {"event": "DOWN", "date": "2023-02-21", "time": "23:41"}
        response = self.client.post(reverse("main"), data=data)
        response2 = self.client.post(reverse("main"), data=data)
        obj = SleepPoint.objects.get(**data)
        self.assertEqual(obj.pk, 1)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response2.status_code, 400)

    def test_delete(self):
        response = self.client.delete(f"/delete/{100}")
        obj = SleepPoint.objects.filter(pk=100)
        self.assertEqual(list(obj), [])
        self.assertEqual(response.status_code, 204)
