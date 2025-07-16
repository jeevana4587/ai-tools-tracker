from django import template

register = template.Library()

@register.filter
def pluck(items, key):
    return [item.get(key) for item in items if key in item]

@register.filter
def int(value):
    try:
        return int(float(value))
    except:
        return 0