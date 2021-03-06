from django import template

register = template.Library()


@register.filter()
def check_permission(user, permission):
	if user.has_perm('auth.%s' % permission):
		return True
	return False
