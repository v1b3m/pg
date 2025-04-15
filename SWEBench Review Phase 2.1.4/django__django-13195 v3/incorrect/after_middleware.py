@@ -42,6 +42,9 @@ class SessionMiddleware(MiddlewareMixin):
                settings.SESSION_COOKIE_NAME,
                path=settings.SESSION_COOKIE_PATH,
                domain=settings.SESSION_COOKIE_DOMAIN,
                secure=settings.SESSION_COOKIE_SECURE or False,
                httponly=settings.SESSION_COOKIE_HTTPONLY or False,
                samesite=settings.SESSION_COOKIE_SAMESITE,
            )
            patch_vary_headers(response, ('Cookie',))
        else: