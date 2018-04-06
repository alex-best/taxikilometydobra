from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy

from .models import Trip
from .forms import CreateTripForm


class TripsList(ListView):
    model = Trip
    context_object_name = 'trips'
    template_name = 'trips/trips-list.html'
    paginate_by = 10

    def get_queryset(self):
        return Trip.objects.filter(user=self.request.user)


class CreateTrip(CreateView):
    form_class = CreateTripForm
    model = Trip
    template_name = 'trips/trips-create.html'
    success_url = reverse_lazy('trips-list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CreateTrip, self).form_valid(form)
