from django import template

from basicoo.apps.core.models import (
	WebsiteStyle)

register = template.Library()


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
	styles = WebsiteStyle.objects.filter(template_name=None).first()

	if styles is not None:
		return "/update-styles/%s/" % (
			styles.id)
	else:
		return "/website-styles/"


@register.simple_tag
def get_styles():
	style_template = WebsiteStyle.objects.filter(
		template_name=None)
	style = None

	for styles in style_template:
		style = styles.template_css_field

		if styles.template:
			style = styles.template.template_css_field

	if style_template and style is not None:
		return style
	else:
		return False


@register.filter
def startswith(value, arg):
	"""Usage, {% if value|starts_with:"arg" %}"""
	return value.startswith(arg)
