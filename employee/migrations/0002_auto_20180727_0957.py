# Generated by Django 2.2 on 2018-07-27 01:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dept',
            old_name='deptno',
            new_name='deptNo',
        ),
        migrations.RenameField(
            model_name='emp',
            old_name='sex',
            new_name='gender',
        ),
        migrations.AlterField(
            model_name='emp',
            name='dept',
            field=models.ForeignKey(db_column='deptNo', on_delete=django.db.models.deletion.CASCADE, to='employee.Dept', to_field='deptno'),
        ),
    ]
