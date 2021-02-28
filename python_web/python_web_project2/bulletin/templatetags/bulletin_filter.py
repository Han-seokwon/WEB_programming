from django import template

register = template.Library()


@register.filter
def sub(value, arg):
    return value - arg

@register.filter
def round_down_by10(value):
    if value%10 == 0:
        value -= 10
    else:
        value -= value%10
    return value

@register.filter
def round_up_by10(value):
    if value%10 != 0:
        value += 10 - value%10
    return value

