from django.contrib import admin
from django.urls import path, include

from main.views import HomeView


urlpatterns = [
    path('', HomeView.as_view(), name='home'),

    path('admin/', admin.site.urls),
]
