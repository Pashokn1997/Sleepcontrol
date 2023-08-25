from apps.sleepcontrolapp.services.service import (
    get_objects_from_db,
    check_existed_data,
    create_new_object,
    delete_object,
)
from django.http import HttpResponseBadRequest
from django.shortcuts import render, redirect

from apps.sleepcontrolapp.forms import SleepForms


def get_data_from_db(request):
    data_from_db = get_objects_from_db()
    return render(
        request,
        "sleepcontrolapp/get_table.html",
        {"data_from_db": data_from_db},
    )


def add_data_to_db(request):
    form = SleepForms()
    if request.method == "POST":
        if check_existed_data(request.POST):
            return HttpResponseBadRequest("Запись уже существует")
        create_new_object(
            event=request.POST["event"],
            date=request.POST["date"],
            time=request.POST["time"],
        )
        return redirect("main")
    return render(
        request, "sleepcontrolapp/form_for_data.html", {"form": form}
    )


def delete_data_from_db(request):
    delete_object(pk=request.POST["pk"])
    return redirect("main")
