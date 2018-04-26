from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import (
	CheckboxInput)

from basicoo import validators

from .models import WebsiteStyle

# Create and import models


class SignUpForm(UserCreationForm):
	password1 = forms.CharField(
		widget=forms.PasswordInput,
		help_text=(
			"The password can't be too similar to the other personal information. \
			The password must contain at least 8 characters. \
			The password can't be a commonly used password. \
			The password can't be entirely numeric."))
	email = forms.EmailField(
		max_length=254,
		help_text='Required. Inform a valid email address.')

	class Meta:
		model = User
		fields = ('username', 'email', 'password1', 'password2', )

	def __init__(self, *args, **kwargs):
		self.user = kwargs.pop('user', None)
		super(SignUpForm, self).__init__(*args, **kwargs)
		for field_name, field in self.fields.items():
			if field.widget.__class__.__name__ != CheckboxInput().__class__.__name__:
				field.widget.attrs['class'] = 'form-control'

	def clean_username(self):
		return self.cleaned_data['username'].capitalize()

	def clean_email(self):
		if User.objects.filter(email__iexact=self.cleaned_data['email']):
			raise forms.ValidationError(validators.DUPLICATE_EMAIL)
		return self.cleaned_data['email']


class CreateStaff(UserCreationForm):
	CHOICES = (
		('client', 'Client'),
		('staff', 'Staff'),
		('admin', 'Admin')
	)

	password1 = forms.CharField(
		widget=forms.PasswordInput,
		help_text=("The password can't be too similar to the other personal information. \
			The password must contain at least 8 characters. \
			The password can't be a commonly used password. \
			The password can't be entirely numeric."))
	permission = forms.ChoiceField(
		choices=CHOICES,
		widget=forms.Select(),
		required=True)
	email = forms.EmailField(
		max_length=254,
		help_text='Required. Inform a valid email address.')

	class Meta:
		model = User
		fields = ('username', 'email', 'password1', 'password2', 'permission', )

	def __init__(self, *args, **kwargs):
		self.user = kwargs.pop('user', None)
		super(CreateStaff, self).__init__(*args, **kwargs)
		for field_name, field in self.fields.items():
			if field.widget.__class__.__name__ != CheckboxInput().__class__.__name__:
				field.widget.attrs['class'] = 'form-control'

	def clean_username(self):
		return self.cleaned_data['username'].capitalize()

	def clean_email(self):
		if User.objects.filter(email__iexact=self.cleaned_data['email']):
			raise forms.ValidationError(validators.DUPLICATE_EMAIL)
		return self.cleaned_data['email']


class UserForm(forms.ModelForm):
	username = forms.CharField(
		max_length=30,
		required=True,
		help_text='Optional.')
	first_name = forms.CharField(
		max_length=254,
		required=False)
	last_name = forms.CharField(
		max_length=254,
		required=False)
	email = forms.EmailField(
		max_length=254,
		required=True,
		help_text='Optional.')

	old_password = forms.CharField(
		max_length=254,
		required=True,
		help_text='This password is a required input to save your data.',
		widget=forms.PasswordInput)
	new_password = forms.CharField(
		max_length=254,
		required=False,
		widget=forms.PasswordInput)
	password_validate = forms.CharField(
		max_length=254,
		required=False,
		widget=forms.PasswordInput)

	address = forms.CharField(
		required=False)
	city = forms.CharField(
		required=False)
	country = forms.CharField(
		required=False)
	postalcode = forms.CharField(
		required=False)

	class Meta:
		model = User
		fields = '__all__'
		exclude = (
			'is_superuser', 'groups', 'user_permissions', 'is_staff',
			'is_active', 'date_joined', 'password', 'last_login',
			'token')

	def __init__(self, *args, **kwargs):
		self.user = kwargs.pop('user', None)
		super(UserForm, self).__init__(*args, **kwargs)
		for field_name, field in self.fields.items():
			if field.widget.__class__.__name__ != CheckboxInput().__class__.__name__:
				field.widget.attrs['class'] = 'form-control'

	def clean_password_validate(self):
		cleaned_data = super(UserForm, self).clean()

		new_password = cleaned_data.get('new_password')
		password_validate = cleaned_data.get('password_validate')

		if new_password and password_validate:
			if new_password != password_validate:
				msg = "The two password fields must match!"
				self.add_error("password_validate", msg)

		return cleaned_data

	def clean_old_password(self):
		cleaned_data = super(UserForm, self).clean()

		old_password = cleaned_data.get('old_password')

		if not self.user.check_password(old_password):
			msg = "Your password is incorrect!"
			self.add_error("old_password", msg)

	def clean_username(self):
		return self.cleaned_data['username'].capitalize()

	def clean_email(self):
		if self.cleaned_data['email'] not in self.user.email and (
			User.objects.filter(
				email__iexact=self.cleaned_data['email'])):
			raise forms.ValidationError(validators.DUPLICATE_EMAIL)

		return self.cleaned_data['email']


class PasswordForgotForm(forms.Form):
	email = forms.EmailField(max_length=254)

	class Meta:
		fields = '__all__'


class PasswordResetForm(forms.Form):
	new_password = forms.CharField(
		max_length=254,
		required=False,
		widget=forms.PasswordInput)
	password_validate = forms.CharField(
		max_length=254,
		required=False,
		widget=forms.PasswordInput)

	class Meta:
		fields = '__all__'

	def clean_password_validate(self):
		cleaned_data = super(PasswordResetForm, self).clean()

		new_password = cleaned_data.get('new_password')
		password_validate = cleaned_data.get('password_validate')

		if new_password and password_validate:
			if new_password != password_validate:
				msg = "The two password fields must match!"
				self.add_error("password_validate", msg)

		return cleaned_data


class StylesForm(forms.ModelForm):
	class Meta:
		model = WebsiteStyle
		fields = '__all__'
		exclude = ('template_css_field',)

	def __init__(self, *args, **kwargs):
		super(StylesForm, self).__init__(*args, **kwargs)
		for field_name, field in self.fields.items():
			if field.widget.__class__.__name__ != CheckboxInput().__class__.__name__:
				field.widget.attrs['class'] = 'form-control'
			else:
				field.widget.attrs['class'] = 'checkbox-control'

			if field_name.endswith('gradient'):
				field.help_text = (
					'This is a gradient, make sure to use following format:' +
					' number example (90deg) make sure to include the "deg"' +
					' behind the number,' +
					' color (, color, you can keep adding colors as' +
					' you please).')
			elif field_name.endswith('color'):
				field.help_text = (
					'Please define a color, you can use' +
					' the color hex, but also the color name.')
			elif field_name is 'save_template':
				field.help_text = (
					'Do you want to save the template?' +
					' Yes / No')
			elif field_name is 'template':
				field.help_text = (
					'Select one of the templates you want to use. \n' +
					'You can also choose not to select any template.')
				field.queryset = WebsiteStyle.objects.all().exclude(template_name=None)
			else:
				field.help_text = (
					'Set a templatename for the template.')
