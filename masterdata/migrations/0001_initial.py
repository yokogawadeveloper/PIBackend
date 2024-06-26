# Generated by Django 3.2.7 on 2021-11-25 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='categoryMaster',
            fields=[
                ('CategoryId', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('CategoryName', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='divisionMaster',
            fields=[
                ('DivisionId', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('DivisionName', models.CharField(max_length=100, null=True)),
                ('BUHead', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='projectManagerMaster',
            fields=[
                ('PMId', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('EmployeeNo', models.CharField(max_length=100, null=True)),
                ('EmployeeName', models.CharField(max_length=100, null=True)),
                ('UpdatedBy', models.CharField(max_length=255, null=True)),
                ('UpdateDate', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='regionMaster',
            fields=[
                ('RegionId', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('RegionName', models.CharField(max_length=100, null=True)),
            ],
        ),
    ]
