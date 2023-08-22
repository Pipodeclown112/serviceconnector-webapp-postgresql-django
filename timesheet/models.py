from django.db import models

# Create your models here.
class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    base_salary = models.IntegerField()
    fte_percentage = models.DecimalField(max_digits=3, decimal_places=2)
    
    # day_rate = 

    def __str__(self):
        return "%s %s", self.first_name, self.last_name
    
class Project(models.Model):
    name = models.CharField(max_length=50)
    time_allocated = models.IntegerField()
    budget_allocated = models.IntegerField()

    working_on = models.ManyToManyField(Employee)

    def __str__(self):
        return self.name
    

