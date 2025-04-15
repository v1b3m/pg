@@ -92,7 +92,13 @@ class CookieStorage(BaseStorage):
                samesite=settings.SESSION_COOKIE_SAMESITE,
            )
        else:
            response.delete_cookie(
                self.cookie_name,
                domain=settings.SESSION_COOKIE_DOMAIN,
                secure=settings.SESSION_COOKIE_SECURE or False,
                httponly=settings.SESSION_COOKIE_HTTPONLY or False,
                samesite=settings.SESSION_COOKIE_SAMESITE,
            )

    def _store(self, messages, response, remove_oldest=True, *args, **kwargs):
        """