# Generated by Django 2.0 on 2017-12-13 02:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0004_auto_20171213_0320'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='trip',
            options={'ordering': ['-created']},
        ),
    ]