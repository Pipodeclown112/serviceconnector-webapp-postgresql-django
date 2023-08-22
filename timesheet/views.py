from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView

from django_tables2 import SingleTableView

from .models import Employee, Project
from .tables import EmployeeTable


def index(request):
    return HttpResponse("Hello, world. You're at the timesheet index.")

class EmployeesView(SingleTableView):
    model = Employee
    table_class = EmployeeTable
    template_name = 'employees.html'
    # employees_list = Employee.objects.order_by("base_data")
    # context = {"employees_list": employees_list}
    # return render(request,"", context)