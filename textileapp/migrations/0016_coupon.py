# Generated by Django 2.2.4 on 2019-10-28 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('textileapp', '0015_delete_coupon'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(default=None, max_length=10)),
                ('price', models.IntegerField(default=None, max_length=6)),
            ],
        ),
    ]
