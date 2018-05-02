import smtplib
import base64

from django.contrib import messages
from django.contrib.auth.mixins import (
	LoginRequiredMixin, PermissionRequiredMixin)
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.utils.http import int_to_base36
from django.conf import settings
from django.urls import reverse

from django.views.generic import (
	CreateView, TemplateView, UpdateView)

from .models import (
	ExtraUserField, WebsiteStyle)
from .forms import (
	CreateStaff, PasswordForgotForm, PasswordResetForm,
	SignUpForm, StylesForm, UserForm)

from .viewfunctions import class_check, css_setter

# Classes for every function in the basic project.


class Signup(CreateView):
	form_class = SignUpForm
	template_name = 'unauthorized/signup.html'

	def get(self, *args, **kwargs):
		self.object = None
		form_class = self.get_form_class()
		form = self.get_form(form_class)
		return self.render_to_response(
			self.get_context_data(form=form))

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

		return HttpResponseRedirect(reverse('core:home'))

	def form_invalid(self, form, request):
		for key, value in form.errors.items():
			messages.error(request, "{0}: {1}".format(key, value))

		return self.render_to_response(
			self.get_context_data(form=form))


class ForgotPassword(TemplateView):
	template_name = 'unauthorized/pw_forgot.html'

	def get(self, *args, **kwargs):
		form = PasswordForgotForm
		return self.render_to_response(
			self.get_context_data(form=form))

	def post(self, request, *args, **kwargs):
		form = PasswordForgotForm(self.request.POST)
		if form.is_valid():
			return self.form_valid(form, request)
		else:
			return self.form_invalid(form, request)

	def form_valid(self, form, request):
		exists = User.objects.filter(email=form.cleaned_data['email']).exists()

		if exists:
			user = User.objects.filter(email=form.cleaned_data['email']).first()
			extra_fields = ExtraUserField.objects.filter(user=user).first()
			token_generator = default_token_generator
			token = token_generator.make_token(user)

			url = 'http://%s/pw-reset/?user_id=%s&token=%s' % (
				request.META['HTTP_HOST'],
				int_to_base36(user.pk),
				token)

			if extra_fields is not None:
				extra_fields.token = token
				extra_fields.save()
			else:
				ExtraUserField.objects.create(
					user=user,
					token=token)

			server = smtplib.SMTP(host=settings.EMAIL_HOST, port=settings.EMAIL_PORT)
			server.ehlo()
			server.starttls()
			server.ehlo()
			server.login(
				settings.SERVER_EMAIL,
				(base64.b64decode(settings.EMAIL_HOST_PASSWORD)).decode('utf-8'))

			header = (
				'To:' + form.cleaned_data['email'] +
				'\n' + 'From: %s' % settings.DEFAULT_FROM_EMAIL +
				'\n' + 'Subject: %s:' % settings.EMAIL_SUBJECT_PREFIX +
				'Reset Password \n')
			msg = header + (
				'\n This is password reset request from %s.com \n %s \n' % (
					settings.PROJECT_NAME,
					url))

			server.sendmail(
				settings.DEFAULT_FROM_EMAIL,
				form.cleaned_data['email'],
				msg)

			server.close()

			return HttpResponseRedirect(reverse('login'))
		else:
			errors = ['This email address does not exist within this website!']

			return self.render_to_response(
				self.get_context_data(
					form=form,
					errors=errors))

	def form_invalid(self, form, request):
		for key, value in form.errors.items():
			messages.error(request, "{0}: {1}".format(key, value))

		return self.render_to_response(
			self.get_context_data(form=form))


class ResetPassword(TemplateView):
	template_name = 'core_pages/submitform.html'

	def get(self, request, *args, **kwargs):
		if 'user_id' in self.request.GET:
			user = User.objects.filter(
				pk=self.request.GET['user_id']).first()
			extra_fields = ExtraUserField.objects.filter(
				token=self.request.GET['token']).first()

			if user and extra_fields:
				form = PasswordResetForm
				formname = 'Password Reset'
				return self.render_to_response(
					self.get_context_data(
						form=form,
						formname=formname))
			else:
				return HttpResponseRedirect(reverse('login'))
		else:
			return HttpResponseRedirect(reverse('login'))

	def post(self, request, *args, **kwargs):
		form = PasswordResetForm(
			self.request.POST)

		user = User.objects.get(pk=self.request.GET['user_id'])
		extra_fields = ExtraUserField.objects.get(token=self.request.GET['token'])

		if form.is_valid():
			return self.form_valid(form, user, extra_fields)
		else:
			return self.form_invalid(form, request)

	def form_valid(self, form, user, extra_fields):
		new_password = form.cleaned_data.get('new_password')
		password_validate = form.cleaned_data.get('password_validate')
		if new_password and password_validate:
			user.set_password(new_password)
			user.save()

		extra_fields.token = ''
		extra_fields.save()

		return HttpResponseRedirect(reverse('login'))

	def form_invalid(self, form, request):
		for key, value in form.errors.items():
			messages.error(request, "{0}: {1}".format(key, value))

		return self.render_to_response(
			self.get_context_data(form=form))


class Home(LoginRequiredMixin, TemplateView):
	template_name = 'core_pages/home.html'


class ViewProfile(LoginRequiredMixin, TemplateView):
	form_class = UserForm
	template_name = 'core_pages/submitform.html'

	def get(self, request, *args, **kwargs):
		user = self.request.user
		fields = ExtraUserField.objects.filter(user=user)
		initials = ''

		if fields is not None:
			for field in fields:
				initials = {
					'address': field.address,
					'city': field.city,
					'country': field.country,
					'postalcode': field.postalcode
				}

			form = UserForm(instance=user, user=user, initial=initials)
		else:
			form = UserForm(instance=user, user=user)

		formname = 'Profile'

		return self.render_to_response(
			self.get_context_data(
				form=form,
				formname=formname))

	def post(self, request, *args, **kwargs):
		user = self.request.user

		form = UserForm(
			self.request.POST,
			instance=user,
			user=user)

		if form.is_valid():
			return self.form_valid(form)
		else:
			return self.form_invalid(form, request)

	def form_valid(self, form):
		self.object = form.save()

		field = ExtraUserField.objects.filter(user=self.request.user)

		if field:
			field.update(
				user=self.request.user,
				address=self.request.POST['address'],
				city=self.request.POST['city'],
				country=self.request.POST['country'],
				postalcode=self.request.POST['postalcode'])
		else:
			field.create(
				user=self.request.user,
				address=self.request.POST['address'],
				city=self.request.POST['city'],
				country=self.request.POST['country'],
				postalcode=self.request.POST['postalcode'])

		new_password = form.cleaned_data.get('new_password')
		password_validate = form.cleaned_data.get('password_validate')
		if new_password and password_validate:
			self.object.set_password(new_password)
			self.object.save()

		return HttpResponseRedirect(reverse('core:view-profile'))

	def form_invalid(self, form, request):
		for key, value in form.errors.items():
			messages.error(request, "{0}: {1}".format(key, value))

		return self.render_to_response(
			self.get_context_data(form=form))


class GetUsers(PermissionRequiredMixin, TemplateView):
	permission_required = 'auth.staff'
	template_name = 'core_pages/get_users.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['users'] = User.objects.all()
		return context


class ViewUser(PermissionRequiredMixin, TemplateView):
	permission_required = 'auth.staff'
	template_name = 'core_pages/view_pages/view_user.html'

	def get(self, request, *args, **kwargs):
		id = request.GET['id']
		user = User.objects.filter(pk=id)
		user_values = user.values()
		extra_values = ExtraUserField.objects.filter(user=user)
		return self.render_to_response(
			self.get_context_data(
				user_values=user_values,
				extra_values=extra_values))

	def post(self, request, *args, **kwargs):
		id = request.GET['id']
		user = User.objects.get(pk=id)
		permission = request.POST['permission']

		class_check(user, permission)

		return HttpResponseRedirect(reverse('core:get-users'))


class BanUser(PermissionRequiredMixin, TemplateView):
	permission_required = 'auth.admin'
	template_name = 'core_pages/action_pages/ban_user.html'

	def get(self, request, *args, **kwargs):
		id = request.GET['id']
		user_values = User.objects.filter(pk=id).values()
		return self.render_to_response(
			self.get_context_data(user_values=user_values))

	def post(self, request, *args, **kwargs):
		id = request.GET['id']
		user = User.objects.get(pk=id)

		if user.is_active:
			user.is_active = False
		else:
			user.is_active = True

		user.save()

		redirect_url = reverse('core:view-user')
		extra_params = '?id=%s' % id if id else ''
		full_redirect_url = '%s%s' % (redirect_url, extra_params)

		return HttpResponseRedirect(full_redirect_url)


class DeleteUser(PermissionRequiredMixin, TemplateView):
	permission_required = 'auth.admin'
	template_name = 'core_pages/action_pages/delete_user.html'

	def get(self, request, *args, **kwargs):
		id = request.GET['id']
		user_values = User.objects.filter(pk=id).values()
		return self.render_to_response(
			self.get_context_data(user_values=user_values))

	def post(self, request, *args, **kwargs):
		id = request.GET['id']
		user = User.objects.get(pk=id)
		user.delete()

		return HttpResponseRedirect(reverse('core:get-users'))


class CreateStaff(PermissionRequiredMixin, CreateView):
	form_class = CreateStaff
	permission_required = 'auth.admin'
	template_name = 'core_pages/submitform.html'

	def get(self, *args, **kwargs):
		self.object = None
		form_class = self.get_form_class()
		form = self.get_form(form_class)
		formname = 'Add Staff'
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

		permission = form.cleaned_data.get('permission')

		class_check(self.object, permission)

		return HttpResponseRedirect(reverse('core:home'))

	def form_invalid(self, form, request):
		for key, value in form.errors.items():
			messages.error(request, "{0}: {1}".format(key, value))

		return self.render_to_response(
			self.get_context_data(form=form))


class CreateStyles(PermissionRequiredMixin, CreateView):
	form_class = StylesForm
	permission_required = 'is_superuser'
	template_name = 'core_pages/submitform.html'

	def get(self, *args, **kwargs):
		styles = WebsiteStyle.objects.filter(
			template_name=None).first()

		if styles is not None:
			return HttpResponseRedirect(reverse('core:home'))
		else:
			self.object = None
			form_class = self.get_form_class()
			form = self.get_form(form_class)
			formname = 'Add Styles'
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

		css_setter(self.object)

		return HttpResponseRedirect(reverse('core:home'))

	def form_invalid(self, form, request):
		for key, value in form.errors.items():
			messages.error(request, "{0}: {1}".format(key, value))

		return self.render_to_response(
			self.get_context_data(form=form))


class UpdateStyles(PermissionRequiredMixin, UpdateView):
	model = WebsiteStyle
	form_class = StylesForm
	permission_required = 'is_superuser'
	template_name = 'core_pages/submitform.html'

	def get(self, *args, **kwargs):
		self.object = self.get_object()
		form = StylesForm(
			instance=WebsiteStyle.objects.get(pk=self.object.id))
		formname = 'Update Styles'
		return self.render_to_response(
			self.get_context_data(
				form=form,
				formname=formname))

	def post(self, request, *args, **kwargs):
		self.object = self.get_object()
		self.styles = WebsiteStyle.objects.get(id=self.object.id)

		form = StylesForm(self.request.POST, instance=self.styles)
		if form.is_valid():
			return self.form_valid(form)
		else:
			return self.form_invalid(form, request)

	def form_valid(self, form):
		self.object = form.save()

		css_setter(self.object)

		if self.object.template_name is not None:
			return HttpResponseRedirect(
				reverse('core:website-styles'))
		else:
			return HttpResponseRedirect(
				reverse('core:update-styles', args=[self.object.id]))

	def form_invalid(self, form, request):
		for key, value in form.errors.items():
			messages.error(request, "{0}: {1}".format(key, value))

		return self.render_to_response(
			self.get_context_data(form=form))
