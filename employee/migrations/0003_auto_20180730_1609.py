# Generated by Django 2.2 on 2018-07-30 08:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0002_auto_20180727_0957'),
    ]

    operations = [
        migrations.RenameField(
            model_name='salegrade',
            old_name='hisal',
            new_name='higsal',
        ),
        migrations.RenameField(
            model_name='salegrade',
            old_name='losal',
            new_name='lowsal',
        ),
        migrations.AlterField(
            model_name='emp',
            name='dept',
            field=models.ForeignKey(db_column='deptNo', on_delete=django.db.models.deletion.CASCADE, to='employee.Dept'),
        ),
    ]