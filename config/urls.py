from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from django.contrib.auth.views import LoginView, LogoutView

from main.views import HomeView
from accounts.views import RegistrationView, ChangePasswordView, ChangeAccountView
from profiles.views import ChangeProfileView
from trips.views import TripsList, CreateTrip


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('login/', LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),
    path('register/', RegistrationView.as_view(), name='register'),

    # Настройки
    path('settings/account', ChangeAccountView.as_view(), name='settings-account'),
    path('settings/profile', ChangeProfileView.as_view(), name='settings-profile'),
    path('settings/password', ChangePasswordView.as_view(), name='settings-password'),

    # Поездки
    path('trips/list', TripsList.as_view(), name='trips-list'),
    path('trips/create', CreateTrip.as_view(), name='trips-create'),

    path('admin/', admin.site.urls),
] 

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
