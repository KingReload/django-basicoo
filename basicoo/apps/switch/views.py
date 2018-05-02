from django.contrib import messages
from django.contrib.auth.mixins import (
	PermissionRequiredMixin)
from django.http import HttpResponseRedirect
from django.conf import settings
from django.urls import reverse

from django.views.generic import (
	CreateView, UpdateView)

from .forms import SwitchForm
from .models import Switch

from basicoo.apps.viewfunctions import switch

# Auto load function

switch(None)

# Classes for every function in the switch project.


class SwitchView(PermissionRequiredMixin, CreateView):
	form_class = SwitchForm
	permission_required = 'is_superuser'
	template_name = 'switch_pages/switch.html'

	def get(self, *args, **kwargs):
		switch = Switch.objects.all().first()

		if switch is not None:
			return HttpResponseRedirect(reverse('core:home'))
		else:
			self.object = None
			form_class = self.get_form_class()
			form = self.get_form(form_class)
			formname = 'Select App'
			return self.render_to_response(
				self.get_context_data(
					form=form,
					formname=formname))

	def post(self, request, *args, **kwargs):
		self.object = None
		form_class = self.get_form_class()
		form = self.get_form(form_class)
		if form.is_valid():
			return self.form_valid(form)
		else:
			return self.form_invalid(form, request)

	def form_valid(self, form):
		self.object = form.save()

		switch(self.object.app1)

		return HttpResponseRedirect(reverse('core:home'))

	def form_invalid(self, form, request):
		for key, value in form.errors.items():
			messages.error(request, "{0}: {1}".format(key, value))

		return self.render_to_response(
			self.get_context_data(form=form))


class UpdateSwitch(PermissionRequiredMixin, UpdateView):
	model = Switch
	form_class = SwitchForm
	permission_required = 'is_superuser'
	template_name = 'switch_pages/switch.html'

	def get(self, *args, **kwargs):
		self.object = self.get_object()
		form_class = self.get_form_class()
		form = self.get_form(form_class)
		formname = 'Select App'
		return self.render_to_response(
			self.get_context_data(
				form=form,
				formname=formname))

	def post(self, request, *args, **kwargs):
		self.object = self.get_object()
		form_class = self.get_form_class()
		form = self.get_form(form_class)
		if form.is_valid():
			return self.form_valid(form)
		else:
			return self.form_invalid(form, request)

	def form_valid(self, form):
		self.object = form.save()

		switch(self.object.app1)

		return HttpResponseRedirect(reverse('core:home'))

	def form_invalid(self, form, request):
		for key, value in form.errors.items():
			messages.error(request, "{0}: {1}".format(key, value))

		return self.render_to_response(
			self.get_context_data(form=form))
