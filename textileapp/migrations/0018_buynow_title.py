# Generated by Django 2.2.4 on 2019-10-29 06:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('textileapp', '0017_auto_20191028_1340'),
    ]

    operations = [
        migrations.AddField(
            model_name='buynow',
            name='title',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='textileapp.Textile'),
        ),
    ]
