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
def get_style(value_type):
	style_templates = WebsiteStyle.objects.all()
	style = None

	for styles in style_templates:
		if styles and not styles.template_name:
			style = getattr(styles, value_type)

			if styles.template:
				style = getattr(styles.template, value_type)

	if style_templates and style is not None:
		return style
	else:
		return False
