from django import template


register = template.Library()


@register.filter
def split(value):
    """Фильтр, который разделяет строку по запятой."""
    return value.split(', ')


@register.filter
def numeric(value):
    """Фильтр, который разделяет число по тысячам."""
    value = f"{value:,}".replace(',', ' ')
    return value
