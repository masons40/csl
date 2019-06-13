from django import template

register = template.Library()

@register.filter()
def About(value):
	return str(value)+"about"

@register.filter()
def Requirements(value):
	return str(value)+"requirements"

@register.filter()
def InitialCreator(value):
	stringValue = str(value).split(" ")
	initials = ""
	for s in stringValue:
		initials+= s[0]
	return initials
