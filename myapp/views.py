from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from .models import Employee


class Index(TemplateView):
    template_name = 'myapp/index.html'

    def get_context_data(self, *args, **kwargs):
      context = super().get_context_data(**kwargs)
      employee_list = Employee.objects.all()
      context = {
          'employee_list': employee_list,
      }
      return context
