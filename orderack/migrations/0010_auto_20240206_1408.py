# Generated by Django 3.2.7 on 2024-02-06 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orderack', '0009_auto_20240206_1134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderacknowledgement',
            name='PI_BasicValuePercentage',
            field=models.IntegerField(default=0.0, null=True),
        ),
        migrations.AlterField(
            model_name='orderacknowledgement',
            name='PI_GstPercentage',
            field=models.IntegerField(default=0.0, null=True),
        ),
    ]