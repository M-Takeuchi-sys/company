from django.urls import path, include
from . import views

app_name = 'myapp'

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('employee_create', views.EmployeeCreate.as_view(), name='employee_create'),
]
