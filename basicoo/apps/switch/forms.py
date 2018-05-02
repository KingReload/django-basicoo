from django import forms
from django.conf import settings
from django.forms import (
	CheckboxInput)

from .models import Switch

# Create and import models


class SwitchForm(forms.ModelForm):
	app1 = forms.ChoiceField()

	class Meta:
		model = Switch
		fields = '__all__'

	def __init__(self, *args, **kwargs):
		list_ = settings.EXTRA_INSTALLED_APPS
		choices = [
			(' ', '----------------')
		]
		super(SwitchForm, self).__init__(*args, **kwargs)

		for item in list_:
			if item.startswith('%s.apps.' % settings.PROJECT_NAME):
				param, value = item.rsplit('.', 1)
				choice = (value, value)
				choices.append(choice)

		for field_name, field in self.fields.items():
			if field.widget.__class__.__name__ != CheckboxInput().__class__.__name__:
				field.widget.attrs['class'] = 'form-control'

			field.choices = choices
			field.label = 'Switch to app:'
			field.help_text = (
				'Here you can select which app you want to switch to.')
