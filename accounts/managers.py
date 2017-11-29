from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    """ Менеджер учётных записей пользователей """

    use_in_migrations = True

    def _create_user(self, phone, password, **extra_fields):
        """ Утилитная функция для создания и сохранения записи. """
        if not phone:
            raise ValueError('Вы должны указать телефон!')
        user = self.model(phone=phone, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, phone, password=None, **extra_fields):
        """ Создаёт нового пользователя. """
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('is_staff', False)
        return self._create_user(phone, password, **extra_fields)

    def create_superuser(self, phone, password, **extra_fields):
        """ Создаёт нового суперпользователя. """
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Суперпользователь должен иметь is_superuser = True.')
        
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Суперпользователь должен иметь is_staff = True.')

        return self._create_user(phone, password, **extra_fields)
