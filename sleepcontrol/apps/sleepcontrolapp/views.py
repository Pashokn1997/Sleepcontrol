from django.http import HttpResponseBadRequest
from django.shortcuts import redirect
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.sleepcontrolapp.forms import SleepForms
from apps.sleepcontrolapp.models import SleepPoint


class SleepPointGetDelete(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "sleepcontrolapp/get_table.html"

    def get(self, request):
        data_from_db = SleepPoint.objects.order_by("date", "time")
        return Response({"data_from_db": data_from_db})

    def post(self, request):
        data_for_delete = SleepPoint.objects.get(pk=request.POST["pk"])
        data_for_delete.delete()
        return redirect("main")


class SleepPointAdd(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "sleepcontrolapp/form_for_data.html"

    def get(self, request):
        form = SleepForms()
        return Response({"form": form})

    def post(self, request):
        form = SleepForms()
        if request.method == "POST":
            if SleepPoint.objects.filter(
                event=request.POST["event"],
                date=request.POST["date"],
                time=request.POST["time"],
            ):
                return HttpResponseBadRequest
            SleepPoint.objects.create(
                event=request.POST["event"],
                date=request.POST["date"],
                time=request.POST["time"],
            )
            return redirect("main")
        return Response({"form": form})
