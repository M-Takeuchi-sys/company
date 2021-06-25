from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, CreateView, DetailView
from .models import Employee
from django.urls import reverse_lazy
from .forms import EmployeeForm


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
