# Generated by Django 2.2.4 on 2019-10-10 07:26

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('textileapp', '0004_auto_20190916_0634'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('totalprice', models.IntegerField(default=None)),
                ('title', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='textileapp.Textile')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]