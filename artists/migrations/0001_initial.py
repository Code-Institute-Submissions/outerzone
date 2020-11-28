# Generated by Django 3.1.3 on 2020-11-23 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('description', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('discogs', models.URLField(blank=True, max_length=1050, null=True)),
                ('soundcloud', models.URLField(blank=True, max_length=1050, null=True)),
            ],
        ),
    ]
