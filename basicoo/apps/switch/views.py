from django.contrib import messages
from django.contrib.auth.mixins import (
	LoginRequiredMixin, PermissionRequiredMixin)
from django.http import HttpResponseRedirect
from django.conf import settings
from django.urls import reverse

from django.views.generic import (
	CreateView, TemplateView, UpdateView)

print(settings.MY_INSTALLED_APPS)

# Classes for every function in the switch project.


class SwitchHome(PermissionRequiredMixin, TemplateView):
	permission_required = 'is_superuser'
	template_name = 'switch_pages/home.html'
