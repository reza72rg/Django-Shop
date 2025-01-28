from django import template

register = template.Library()

@register.filter
def format_price(value, currency='تومان'):
    try:
        formatted_price = "{:,}".format(value)
        return f"{formatted_price} {currency}"
    except (ValueError, TypeError):
        return value
