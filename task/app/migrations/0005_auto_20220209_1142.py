# Generated by Django 3.0.7 on 2022-02-09 08:42

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0004_auto_20220209_1114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='users',
            field=models.ManyToManyField(related_name='reports', to=settings.AUTH_USER_MODEL),
        ),
    ]