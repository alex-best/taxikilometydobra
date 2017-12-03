from django.contrib import admin

from .models import FamilyProfile


class FamilyProfileAdmin(admin.ModelAdmin):
    """ Модель отображения учетной записи пользователя в админ-панели Django """

    list_display = ('user', )
    fieldsets = (
        (None, {
            'fields': ('user', )
        }),
        ('Дополнительно', {
            'fields': ('trips_per_month', 'car_requirements', 'info'),
        }),
    )

admin.site.register(FamilyProfile, FamilyProfileAdmin)
