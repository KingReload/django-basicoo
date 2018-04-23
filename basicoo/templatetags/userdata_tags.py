from django.contrib.auth.models import User
from django import template

from basicoo.apps.core.models import (
	WebsiteStyle)

register = template.Library()


@register.simple_tag
def get_username_from_userid(user_id):
	try:
		return User.objects.get(id=user_id).username
	except User.DoesNotExist:
		return 'Unknown'


@register.simple_tag
def get_email_from_userid(user_id):
	try:
		return User.objects.get(id=user_id).email
	except User.DoesNotExist:
		return 'Unknown'


@register.filter()
def check_permission(user, permission):
	if user.user_permissions.filter(codename=permission).exists():
		return True

	return False


@register.simple_tag
def htmlattributes(value, arg):
	attrs = value.field.widget.attrs

	kvs = arg.split(',')

	for string in kvs:
		kv = string.split(':')
		attrs[kv[0]] = kv[1]

	rendered = str(value)

	return rendered


register.filter('htmlattributes', htmlattributes)


@register.simple_tag
def check_styles():
	styles = WebsiteStyle.objects.all().first()

	if styles is not None:
		return "/update-styles/%s/" % (
			styles.id)
	else:
		return "/website-styles/"


@register.simple_tag
def get_style(value_type):
	styles = WebsiteStyle.objects.all().first()
	style = getattr(styles, value_type)

	if styles and style:
		return style
	else:
		return None
