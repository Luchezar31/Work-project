from django import template

register = template.Library()

@register.filter
def placeholder(value,name_of_placeholder):
    value.field.widget.attrs['placeholder'] = name_of_placeholder
    return value