from django import template
from googletrans import Translator
import hashlib
from django.core.cache import cache


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

def make_cache_key(text, lang):
    raw = f"{text}:{lang}"
    return "trans:" + hashlib.md5(raw.encode("utf-8")).hexdigest()

@register.filter
def translate(text, target_lang):
    # if not text or not target_lang:
    #     return text

    # cache_key = make_cache_key(text, target_lang)
    # cached = cache.get(cache_key)
    # if cached:
    #     return cached

    # try:
    #     from capstone.tasks import background_translate_and_cache
    #     background_translate_and_cache.delay(text, target_lang)
    # except Exception as e:
    #     print(f"Background translation not triggered: {e}")

    return text
