# Generated by Django 3.2.7 on 2022-01-21 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('excelupload', '0003_auto_20211214_1651'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proformaitemmaster',
            name='PaymentTerms',
            field=models.CharField(max_length=355, null=True),
        ),
    ]