from django.contrib.auth.models import Permission
from django.conf import settings

from basicoo.apps.switch.models import Switch

# Definitions to get the same outcome used for multiple classes.


def class_check(user, permission):
	permission_array = [
		Permission.objects.get(codename='client').id,
		Permission.objects.get(codename='staff').id,
		Permission.objects.get(codename='admin').id,
	]

	permissions = []

	if permission == 'client':
		user.is_staff = False
		permissions = [
			'client'
		]
	if permission == 'staff':
		user.is_staff = True
		permissions = [
			'staff'
		]
	if permission == 'admin':
		user.is_staff = True
		permissions = [
			'staff',
			'admin'
		]

	for d in permission_array:
		user.user_permissions.remove(d)

	if permissions is not None:
		for a in permissions:
			perm = Permission.objects.get(codename=a).id
			user.user_permissions.add(perm)

	user.save()

	return user


def css_setter(object_):
	file_ = open(settings.FILE_PATH)
	object_.template_css_field = (
		('%s' % file_.read()) % (
			object_.navbar_gradient,
			object_.navbar_gradient,
			object_.navbar_text_color,
			object_.navbar_text_color,
			object_.navbar_text_color,
			object_.navbar_text_hover_color,
			object_.navbar_hover_color,
			object_.body_gradient,
			object_.body_text_color,
			object_.footer_color,
			object_.footer_text_color,
			object_.button_color,
			object_.button_text_color,
			object_.button_text_hover_color,
			object_.button_hover_color))

	object_.save()

	return object_


def check_space(value):
	if not value.isspace():
		return True
	else:
		return False


def switch(value):
	switch = None

	if value is None:
		switch = Switch.objects.all().first()

	if switch is not None or value is not None:
		if switch is not None:
			app1 = switch.app1
			boolean = check_space(switch.app1)
		else:
			app1 = value
			boolean = check_space(value)
		
		if boolean:
			app = '%s.apps.%s' % (settings.PROJECT_NAME, app1)
			settings.SWITCH_APPS = []
			settings.SWITCH_APPS.append(app)
		else:
			settings.SWITCH_APPS = []
