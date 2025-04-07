from django import template

register = template.Library()


@register.filter(name='multiply_2_numbers')
def multiply_2_numbers(first, second):
    return first * second
