
from django import http
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from django.core.urlresolvers import reverse

from registration import forms
from registration import models
from registration import get_site

class Register(FormView):
    template_name = 'registration/register.html'
    form_class = forms.RegistrationForm
    
    def get_success_url(self):
        if self.success_url:
            return self.success_url
        return reverse("registration_complete")

    def form_valid(self, form):
        # activate user...
        models.RegistrationProfile.objects.create_inactive_user(
            form.cleaned_data['first_name'],
            form.cleaned_data['last_name'],
            form.cleaned_data['username'],
            form.cleaned_data['password1'],
            form.cleaned_data['email'],
            get_site(self.request)
        )
        return super(Register, self).form_valid(form)

class RegistrationComplete(TemplateView):
    template_name = 'registration/registration_complete.html'

class ActivationComplete(TemplateView):
    template_name = 'registration/activation_complete.html'

class Activate(TemplateView):
    template_name = 'registration/activation_failed.html'

    def get(self, request, *args, **kwargs):
        new_user = models.RegistrationProfile.objects.activate_user(kwargs['activation_key'])
        if new_user:
            return http.HttpResponseRedirect(reverse("registration_activation_complete"))
        return super(Activate, self).get(request, *args, **kwargs)

def logout_view(request):
    logout(request)
    return redirect('/')