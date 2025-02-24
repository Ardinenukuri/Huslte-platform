from django import template

register = template.Library()

@register.filter
def get_item(dictionary, key):
    """Custom template filter to access dictionary keys safely"""
    return dictionary.get(key, None) if dictionary else None
