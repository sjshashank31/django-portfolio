# Generated by Django 2.2.10 on 2020-05-31 04:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_auto_20200531_0908'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='about',
            field=models.TextField(blank=True, null=True),
        ),
    ]
