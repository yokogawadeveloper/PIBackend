# Generated by Django 3.2.7 on 2021-12-31 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='category',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='division',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='project_manager',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='region',
            field=models.IntegerField(null=True),
        ),
    ]
