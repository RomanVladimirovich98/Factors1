from django import template

register = template.Library()

@register.filter
def get_item(dictionary, key):
   """Получить элемент словаря по ключу, возвращая None, если ключ не найден."""
   return dictionary.get(key)