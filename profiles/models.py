from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver


class FamilyProfile(models.Model):
    """ Модель профиля для учётной записи пользователя """

    class Meta:
        verbose_name = "Профиль семьи"
        verbose_name_plural = "Профили семей"

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')
    trips_per_month = models.PositiveIntegerField(verbose_name='Необходимое количество поездок в месяц', blank=True, null=True)
    car_requirements = models.TextField(verbose_name='Требования к машине', blank=True)
    info = models.TextField(verbose_name='Дополнительно', max_length=500, blank=True)


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_user_profile(sender, instance, created, **kwargs):
    if created and not instance.is_staff:
        FamilyProfile.objects.create(user=instance)
