    no middleware leaks an exception and that the next middleware in the stack
    can rely on getting a response instead of an exception.
    """
    if asyncio.iscoroutinefunction(get_response):
        @wraps(get_response)
        async def inner(request):
            try: