from apps.sleepcontrolapp.service import (
    get_events,
    events_exists,
    create_event,
    delete_event,
)
from django.http import HttpResponseBadRequest
from django.shortcuts import render, redirect

from apps.sleepcontrolapp.forms import SleepForms


def get_data(request):
    events = get_events()
    return render(
        request,
        "sleepcontrolapp/get_table.html",
        {"events": events},
    )


def add_event(request):
    if request.method == "POST":
        form = SleepForms(request.POST)
        if events_exists(event=request.POST['event'], date=request.POST['date'], time=request.POST['time']):
            return HttpResponseBadRequest("Запись уже существует")
        if form.is_valid():
            print(form.cleaned_data)
            create_event(
                event=form.cleaned_data["event"],
                date=form.cleaned_data["date"],
                time=form.cleaned_data["time"],
            )
        return redirect("main")
    form = SleepForms()
    return render(
        request, "sleepcontrolapp/form_for_data.html", {"form": form}
    )


def delete_data(request):
    delete_event(pk=request.POST["pk"])
    return redirect("main")
