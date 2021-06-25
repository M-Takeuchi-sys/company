from django.urls import path, include
from . import views

app_name = 'myapp'

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('employee_create', views.EmployeeCreate.as_view(), name='employee_create'),
    path('employee_detail/<int:pk>', views.EmployeeDetail.as_view(), name='employee_detail'),
    path('employee_update/<int:pk>', views.EmployeeUpdate.as_view(), name='employee_update'),
    path('employee_delete/<int:pk>', views.EmployeeDelete.as_view(), name='employee_delete'),
]
