# Generated by Django 2.2.4 on 2019-10-25 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('textileapp', '0012_buynow'),
    ]

    operations = [
        migrations.AddField(
            model_name='buynow',
            name='email',
            field=models.EmailField(default=None, max_length=254),
        ),
        migrations.AddField(
            model_name='buynow',
            name='firstname',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AddField(
            model_name='buynow',
            name='lastname',
            field=models.CharField(default=None, max_length=100),
        ),
    ]
