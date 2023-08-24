from django.http import HttpResponseBadRequest
from django.shortcuts import redirect
from django.views.generic import ListView, FormView, DeleteView

from apps.sleepcontrolapp.forms import SleepForms
from apps.sleepcontrolapp.models import SleepPoint


class GetDataFromDb(ListView):
    queryset = SleepPoint.objects.all()
    template_name = "sleepcontrolapp/get_table.html"
    context_object_name = "data_from_db"

    def get_queryset(self):
        return self.queryset.order_by("date", "time")


class SleepFormsViews(FormView):
    template_name = "sleepcontrolapp/form_for_data.html"
    form_class = SleepForms
    success_url = "/get/"

    def form_valid(self, form):
        if SleepPoint.objects.filter(**form.cleaned_data):
            return HttpResponseBadRequest("Запись уже существует")
        SleepPoint.objects.create(**form.cleaned_data)
        return redirect(self.get_success_url())


class DeleteDataFromDb(DeleteView):
    model = SleepPoint
    success_url = "/get/"

    def get_object(self, queryset=None):
        pk = self.request.POST["pk"]
        return self.get_queryset().get(pk=pk)
