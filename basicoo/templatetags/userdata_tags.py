from django.contrib.auth.models import User
from django import template

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
