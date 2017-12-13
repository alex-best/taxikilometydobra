from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import FormView, DetailView
from django.urls import reverse_lazy
from django.contrib import messages

from .forms import ProfileChangeForm
from .models import Profile

class ChangeProfileView(LoginRequiredMixin, FormView):
    """ Страница содержащая форму смены информации """

    login_url = '/login/'
    redirect_field_name = 'redirect'
    form_class = ProfileChangeForm
    template_name = 'settings/settings-profile.html'
    success_url = reverse_lazy('settings-profile')

    def get_form(self):
        return self.form_class(instance=self.request.user.profile, **self.get_form_kwargs())

    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'Информация профиля изменена!')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Пожалуйста, проверьте введённые данные!')
        return self.render_to_response(self.get_context_data(form=form))


class ProfileDetail(DetailView):
    model = Profile
    template_name = 'profiles/profile-details.html'

    def get_object(self, queryset=None):
        return self.request.user.profile