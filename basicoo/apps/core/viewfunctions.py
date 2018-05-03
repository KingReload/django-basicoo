import datetime

from django.contrib.auth.models import Permission
from django.contrib import messages
from django.conf import settings

from .models import Log

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
	file_ = open(settings.STYLING_FILE)
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


def create_log(user1, user2, word1, word2, permission):

	log_action = '%s user: %s' % (word1, user2.username)
	log = (
		'%s with id ( %s ) and email ( %s ) %s' +
		' user %s with id ( %s ) and email ( %s )') % (
			user1.username,
			user1.id,
			user1.email,
			word2,
			user2.username,
			user2.id,
			user2.email)

	if permission is not None:
		log = log + ' with permisson ( %s )' % (
			permission)

	html_format = (
		'<tr class="log"> \n' +
		'\t <td class="log_action"> \n' +
		'\t\t <span class="action">' + log_action + '</span> \n' +
		'\t\t <span class="time">' + str(datetime.datetime.now()) + '</span> \n' +
		'\t </td> \n' +
		'\t <td class="log_text">' + log + '</td> \n' +
		'</tr> \n')

	file_ = open(settings.LOG_FILE, 'a+')
	file_info = file_.read()
	file_.write(file_info + html_format)
	file_.close()

	Log.objects.create(
		log_action=log_action,
		user=user1,
		log=log)

	pass


def form_invalid(self, form, request):
	for key, value in form.errors.items():
		messages.error(request, "{0}: {1}".format(key, value))

	return self.render_to_response(
		self.get_context_data(form=form))
