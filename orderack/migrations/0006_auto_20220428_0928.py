# Generated by Django 3.2.7 on 2022-04-28 03:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('orderack', '0005_alter_orderacknowledgementhistory_partname'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderacknowledgement',
            name='UpdatedBy',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='orderacknowledgement',
            name='UpdatedDate',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='orderacknowledgement',
            name='deleted_remarks',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
