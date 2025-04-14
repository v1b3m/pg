@@ -498,6 +498,14 @@ def safeseq(value):
    return [mark_safe(obj) for obj in value]


@register.filter(is_safe=True)
def escapeseq(value):
    """
    Escape each element in the sequence.
    """
    return [escape(obj) for obj in value]


@register.filter(is_safe=True)
@stringfilter
def striptags(value):