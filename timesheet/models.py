from django.db import models

# Create your models here.
class Employee(models.Model):
    first_name = models.CharField(max_length=50, default="")
    last_name = models.CharField(max_length=50, default="")
    base_salary = models.IntegerField(default=0)
    fte_percentage = models.DecimalField(max_digits=3, decimal_places=2, default=1)
    # NO_WORKING_DAYS = 52*5
    # day_rate = models.IntegerField(default=base_salary / (NO_WORKING_DAYS * fte_percentage))

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
   
class Project(models.Model):
    name = models.CharField(max_length=50, default="")
    time_allocated = models.IntegerField()
    budget_allocated = models.IntegerField()

    working_on = models.ManyToManyField(Employee)

    def __str__(self):
        return self.name
    

