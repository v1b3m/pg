    return [mark_safe(obj) for obj in value]


@register.filter(is_safe=True)
@stringfilter
def striptags(value):