# Generated by Django 2.0 on 2017-12-08 03:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='lists',
            new_name='todo_list',
        ),
    ]
