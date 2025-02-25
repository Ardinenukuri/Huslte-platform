from django import template

register = template.Library()

@register.filter
def get_item(dictionary, key):
    """Returns the dictionary value for the given key."""
    return dictionary.get(key, None)
