# Generated by Django 2.2.10 on 2020-05-30 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_study'),
    ]

    operations = [
        migrations.AlterField(
            model_name='study',
            name='cgpa_or_percent',
            field=models.DecimalField(decimal_places=2, max_digits=4),
        ),
    ]
