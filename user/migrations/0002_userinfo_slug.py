# Generated by Django 2.0 on 2018-05-31 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='slug',
            field=models.SlugField(default=''),
        ),
    ]
