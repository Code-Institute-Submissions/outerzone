# Generated by Django 3.1.3 on 2020-11-18 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20201118_2051'),
    ]

    operations = [
        migrations.AddField(
            model_name='artist',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='artist',
            name='discogs',
            field=models.URLField(blank=True, max_length=1050, null=True),
        ),
        migrations.AddField(
            model_name='artist',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='artist',
            name='soundcloud',
            field=models.URLField(blank=True, max_length=1050, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]