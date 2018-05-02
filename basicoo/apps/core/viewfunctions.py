from django.contrib.auth.models import Permission
from django.conf import settings

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


def form_invalid(self, form, request):
	for key, value in form.errors.items():
		messages.error(request, "{0}: {1}".format(key, value))

	return self.render_to_response(
		self.get_context_data(form=form))
