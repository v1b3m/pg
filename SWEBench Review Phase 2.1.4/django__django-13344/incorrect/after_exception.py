@@ -31,7 +31,10 @@ def convert_exception_to_response(get_response):
    no middleware leaks an exception and that the next middleware in the stack
    can rely on getting a response instead of an exception.
    """
    # Treat get_response as async if it's a coroutine function or if it's an object whose get_response attr is a coroutine function.
    if asyncio.iscoroutinefunction(get_response) or (
        not asyncio.iscoroutinefunction(get_response) and hasattr(get_response, 'get_response') and asyncio.iscoroutinefunction(get_response.get_response)
    ):
        @wraps(get_response)
        async def inner(request):
            try: