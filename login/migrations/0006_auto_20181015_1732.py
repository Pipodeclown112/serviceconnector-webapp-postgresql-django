# Generated by Django 2.1 on 2018-10-15 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0005_employee_username'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='City',
            new_name='Password',
        ),
        migrations.RenameField(
            model_name='employee',
            old_name='Job_Title',
            new_name='Team',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='Address',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='Business_Phone',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='Company',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='Country_Region',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='Fax_Number',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='Home_Phone',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='Mobile_Phone',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='Notes',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='State_Province',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='Web_Page',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='ZIP',
        ),
        migrations.AddField(
            model_name='employee',
            name='Active',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]
