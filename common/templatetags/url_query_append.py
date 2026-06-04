from django import template

register = template.Library()

@register.simple_tag(takes_context=True)
def url_query_append(context,field,value):
    query_param = context['request'].GET.copy()
    query_param[field] = value
    return query_param.urlencode()

