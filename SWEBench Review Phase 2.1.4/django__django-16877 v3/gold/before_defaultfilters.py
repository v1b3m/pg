    return conditional_escape(value)


@register.filter(is_safe=True)
@stringfilter
def force_escape(value):