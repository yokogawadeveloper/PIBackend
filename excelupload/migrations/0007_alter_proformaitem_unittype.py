# Generated by Django 3.2.7 on 2023-12-04 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('excelupload', '0006_alter_proformaitem_qtymodels'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proformaitem',
            name='UnitType',
            field=models.CharField(default='INR', max_length=255, null=True),
        ),
    ]
