from django.urls import path

from . import views
from timesheet.views import EmployeesView

app_name='timesheet'
urlpatterns = [
    path("", views.index, name="index"),
    path("employees", EmployeesView.as_view(), name="employees")
]