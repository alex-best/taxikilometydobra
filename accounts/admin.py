from django.contrib import admin

from .models import User


class UserAdmin(admin.ModelAdmin):
    """ Модель отображения учетной записи пользователя в админ-панели Django """

    list_display = ('phone', 'first_name', 'last_name')
    fieldsets = (
        (None, {
            'fields': ('phone', 'first_name', 'last_name', 'avatar')
        }),
        ('Дополнительно', {
            'fields': ('is_staff', 'is_superuser', 'is_active'),
        }),
    )

admin.site.register(User, UserAdmin)
