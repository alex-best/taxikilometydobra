from django.shortcuts import render
from django.db.models import Sum
from django.views.generic import TemplateView

from trips.models import Trip, TripStatus
from profiles.models import FamilyProfile


class HomeView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context["trips_number"] = Trip.objects.filter(status=TripStatus.COMPLETED).count()
        context["family_number"] = FamilyProfile.objects.count()
        context["req"] = FamilyProfile.objects.aggregate(Sum('trips_per_month'))['trips_per_month__sum']
        return context
