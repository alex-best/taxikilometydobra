# Generated by Django 2.0rc1 on 2017-11-29 11:07

import accounts.utils
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_user_is_staff'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'Пользователь', 'verbose_name_plural': 'Пользователи'},
        ),
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to=accounts.utils.get_file_path, verbose_name='аватар'),
        ),
        migrations.AlterField(
            model_name='user',
            name='date_joined',
            field=models.DateTimeField(auto_now_add=True, help_text='Дата регистрации пользователя.', verbose_name='зарегистрирован'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(default=True, help_text='Используется для блокировки пользователя без удаления.', verbose_name='активен'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_staff',
            field=models.BooleanField(default=False, help_text='Используется фреймворком для проверки доступа в админ-панель.', verbose_name='администратор'),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(max_length=15, unique=True, validators=[django.core.validators.RegexValidator(message="Телефон должен быть введён в формате: '+999999999'. От 9 до 15 символов.", regex='^\\+?1?\\d{9,15}$')], verbose_name='телефон'),
        ),
    ]
