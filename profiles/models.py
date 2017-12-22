from django.db import models
from django.conf import settings


class UserTypes:
    STAFF = 'STAFF'
    FAMILY = 'FAMILY'
    BENEFACTOR = 'BENEFACTOR'
    
    CHOICES = (
        (STAFF, 'Сотрудник'),
        (BENEFACTOR, 'Благотворитель'),
        (FAMILY, 'Семья'),
    )

class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')
    user_type = models.CharField(max_length=15, choices=UserTypes.CHOICES, default=UserTypes.BENEFACTOR)

    class Meta:
        abstract = True


class StaffProfile(models.Model):
    position = models.CharField(verbose_name='Позиция', max_length=30, blank=True)

    class Meta:
        abstract = True


class FamilyProfile(models.Model):
    trips_per_month = models.PositiveIntegerField(verbose_name='Необходимое количество поездок в месяц', blank=True)
    car_requirements = models.TextField(verbose_name='Требования к машине', blank=True)
    info = models.TextField(verbose_name='Дополнительно', max_length=500, blank=True)

    class Meta:
        abstract = True


class BenefactorProfile(models.Model):
    about = models.TextField(verbose_name='О себе', max_length=500, blank=True)

    class Meta:
        abstract = True


class Profile(UserProfile, StaffProfile, FamilyProfile, BenefactorProfile):
    pass

