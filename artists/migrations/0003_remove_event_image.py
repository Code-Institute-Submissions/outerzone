# Generated by Django 3.1.3 on 2020-11-27 18:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('artists', '0002_event'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='image',
        ),
    ]
