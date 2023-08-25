from django.http import HttpResponseBadRequest
from django.shortcuts import render, redirect

from apps.sleepcontrolapp.forms import SleepForms
from apps.sleepcontrolapp.models import SleepPoint


def get_data_from_db(request):
    data_from_db = SleepPoint.objects.order_by("date", "time")
    return render(
        request,
        "sleepcontrolapp/get_table.html",
        {"data_from_db": data_from_db},
    )


def add_data_to_db(request):
    form = SleepForms()
    if request.method == "POST":
        if SleepPoint.objects.filter(
            event=request.POST["event"],
            date=request.POST["date"],
            time=request.POST["time"],
        ):
            return HttpResponseBadRequest("Запись уже существует")
        SleepPoint.objects.create(
            event=request.POST["event"],
            date=request.POST["date"],
            time=request.POST["time"],
        )
        return redirect("main")
    return render(
        request, "sleepcontrolapp/form_for_data.html", {"form": form}
    )


def delete_data_from_db(request):
    data_for_delete = SleepPoint.objects.get(pk=request.POST["pk"])
    data_for_delete.delete()
    return redirect("main")
