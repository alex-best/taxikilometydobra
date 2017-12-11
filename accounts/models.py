from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.core.validators import RegexValidator

from .managers import UserManager
from .utils import get_file_path


class User(AbstractBaseUser, PermissionsMixin):
    """ Модель учётной записи пользователя """

    phone_regex = RegexValidator(
        regex=r'^\+\d{9,15}$',  
        message="Неверный формат телефона!"
    )

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    phone = models.CharField('телефон', max_length=15, unique=True, validators=[phone_regex])
    first_name = models.CharField('имя', max_length=30, blank=True)
    last_name = models.CharField('фамилия', max_length=30, blank=True)
    avatar = models.ImageField('аватар', upload_to=get_file_path, null=True, blank=True)

    date_joined = models.DateTimeField('зарегистрирован', auto_now_add=True, help_text='Дата регистрации пользователя.')
    is_active = models.BooleanField('активен', default=True, help_text='Используется для блокировки пользователя без удаления.')
    is_staff = models.BooleanField('администратор', default=False, help_text='Используется фреймворком для проверки доступа в админ-панель.')

    objects = UserManager()

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def get_full_name(self):
        """ Возвращает полное имя без крайних пробелов, либо телефон, если имя и фамилия не указаны """
        if self.first_name or self.last_name:
            full_name = '%s %s' % (self.first_name, self.last_name)
        else:
            full_name = self.phone
        return full_name.strip()

    def get_short_name(self):
        """ Возвращает короткое имя (только имя) """
        return self.first_name
