from django import template
from django.template.defaultfilters import stringfilter
from users.translations import translate

register = template.Library()

@register.filter
@stringfilter
def translate_text(value, language='en'):
    """
    Template filter to translate text
    Usage: {{ "Settings"|translate_text:user_language }}
    """
    return translate(value, language)

@register.simple_tag(takes_context=True)
def t(context, text):
    """
    Template tag to translate text
    Usage: {% t "Settings" %}
    """
    language = context.get('user_language', 'en')
    return translate(text, language) 