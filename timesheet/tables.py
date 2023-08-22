import django_tables2 as tables
from .models import Employee

class EmployeeTable(tables.Table):
    class Meta:
        model = Employee
        template_name = "django_tables2/bootstrap.html"
        fields = ("first_name", "last_name", "base_salary", "fte_percentage",)