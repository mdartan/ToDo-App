# Generated by Django 3.0.7 on 2022-02-09 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_todo_updated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='Status',
            field=models.CharField(choices=[('Complete', 'Complete'), ('Not Complete', 'Not Complete')], max_length=200, null=True),
        ),
    ]
