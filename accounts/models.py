from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser

from .managers import UserManager
from .utils import get_file_path


class User(AbstractBaseUser, PermissionsMixin):
    """ Модель учётной записи пользователя """
    
    phone = models.CharField('телефон', max_length=15, unique=True)
    first_name = models.CharField('имя', max_length=30, blank=True)
    last_name = models.CharField('фамилия', max_length=30, blank=True)
    avatar = models.ImageField('аватар', upload_to=get_file_path, null=True, blank=True)

    date_joined = models.DateTimeField('зарегистрирован', auto_now_add=True)
    is_active = models.BooleanField('активен', default=True)
    is_staff = models.BooleanField('администратор', default=False)

    objects = UserManager()

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def get_full_name(self):
        """ Возвращает полное имя без крайних пробелов """
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        """ Возвращает короткое имя (только имя) """
        return self.first_name
