from django import template 

register = template.Library()

@register.filter(name='cut')
def cut(value,arg):
	""" removes all values of "arg' from the value passed in."""

	return value.replace(arg,'')

# register.filter('cut',cut) #string you use to call the function, and the function you wish to call.