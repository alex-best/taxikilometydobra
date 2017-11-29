# Generated by Django 2.0rc1 on 2017-11-29 11:40

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20171129_1407'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(max_length=15, unique=True, validators=[django.core.validators.RegexValidator(message='Неверный формат телефона!', regex='^\\+\\d{9,15}$')], verbose_name='телефон'),
        ),
    ]
