from django import template
from googletrans import Translator

register = template.Library()
translator = Translator() 

@register.filter
def get_item(dictionary, key):
    """Custom template filter to access dictionary keys safely"""
    return dictionary.get(key, None) if dictionary else None

@register.filter(name="get_dict_value")
def get_dict_value(dictionary, key):
    """Returns the value from a dictionary based on a given key."""
    return dictionary.get(key, "") if isinstance(dictionary, dict) else ""


@register.filter
def translate(text, target_lang):
    if not text or not target_lang:
        return text

    # Simple in-memory cache (reset on server reload)
    if not hasattr(translate, 'memory_cache'):
        translate.memory_cache = {}

    cache_key = f"{text}_{target_lang}"
    if cache_key in translate.memory_cache:
        return translate.memory_cache[cache_key]

    try:
        translation = translator.translate(text, dest=target_lang)
        translate.memory_cache[cache_key] = translation.text
        return translation.text
    except Exception as e:
        print(f"Translation failed: {e}")
        return text
