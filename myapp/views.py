from django.shortcuts import render, resolve_url
from django.http import HttpResponse
from django.views.generic import TemplateView, CreateView, DetailView, UpdateView
from .models import Employee
from django.urls import reverse_lazy
from .forms import EmployeeForm
from django.contrib import messages


class Index(TemplateView):
    template_name = 'myapp/index.html'

    def get_context_data(self, *args, **kwargs):
      context = super().get_context_data(**kwargs)
      employee_list = Employee.objects.all()
      context = {
          'employee_list': employee_list,
      }
      return context

class EmployeeCreate(CreateView):
    model = Employee
    form_class = EmployeeForm
    success_url = reverse_lazy('myapp:index')

class EmployeeDetail(DetailView):
    model = Employee

class EmployeeUpdate(UpdateView):
    model = Employee
    form_class = EmployeeForm

    def get_success_url(self):
        messages.info(self.request, '社員情報を更新しました。')
        return resolve_url('myapp:employee_detail', pk=self.kwargs['pk'])
