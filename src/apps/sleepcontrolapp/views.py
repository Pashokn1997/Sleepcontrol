from apps.sleepcontrolapp import service
from django.http import HttpResponseBadRequest
from django.shortcuts import render, redirect

from apps.sleepcontrolapp.forms import SleepForms


def get_events(request):
    events = service.get_events()
    return render(
        request,
        "sleepcontrolapp/get_table.html",
        {"events": events},
    )


def add_event(request):
    form = SleepForms()
    if request.method == "POST":
        form = SleepForms(request.POST)
        if form.is_valid():
            if service.event_exists(**form.cleaned_data):
                return HttpResponseBadRequest("Запись уже существует")
            service.create_event(**form.cleaned_data)
            return redirect("main")
    return render(
        request, "sleepcontrolapp/form_for_data.html", {"form": form}
    )


def delete_event(request):
    service.delete_event(pk=request.POST["pk"])
    return redirect("main")
