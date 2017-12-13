# Generated by Django 2.0 on 2017-12-13 00:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0003_trip_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trip',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Создана'),
        ),
        migrations.AlterField(
            model_name='trip',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
