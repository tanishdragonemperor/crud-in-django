# Generated by Django 3.0.4 on 2021-04-26 10:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0020_auto_20210426_1616'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='donors',
            name='vehicles',
        ),
    ]
