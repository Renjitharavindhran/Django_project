# Generated by Django 2.2.4 on 2019-10-16 06:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('textileapp', '0010_auto_20191014_1220'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='colour',
        ),
    ]