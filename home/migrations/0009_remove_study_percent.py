# Generated by Django 2.2.10 on 2020-05-30 09:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_auto_20200530_1429'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='study',
            name='percent',
        ),
    ]
