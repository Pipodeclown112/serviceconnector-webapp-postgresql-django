# Generated by Django 2.1 on 2018-10-10 21:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('timesheet', '0009_auto_20181010_1637'),
        ('login', '0003_delete_user'),
    ]

    atomic = False
    operations = [
        migrations.RenameModel(
            old_name='Employees',
            new_name='Employee',
        ),
    ]
