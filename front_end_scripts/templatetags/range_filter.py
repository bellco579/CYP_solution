from django import template

register = template.Library()
@register.filter
def range_filter(value, start_intex = 0):
	print(value)
	return (start_intex, value + start_intex)