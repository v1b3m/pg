@@ -210,12 +210,19 @@ class HttpResponseBase:
        value = signing.get_cookie_signer(salt=key + salt).sign(value)
        return self.set_cookie(key, value, **kwargs)

    def delete_cookie(self, key, path='/', domain=None, secure=None, httponly=False, samesite=None):
        """
        Delete a cookie by setting its max_age to 0 and expiration date to the past.
        Optionally specify secure, httponly, and samesite attributes to match the original cookie.
        If secure is None, it will be set to True if the cookie name starts with __Secure- or __Host-.
        """
        if secure is None:
            secure_flag = key.startswith(('__Secure-', '__Host-'))
        else:
            secure_flag = bool(secure)
        self.set_cookie(
            key, '', max_age=0, path=path, domain=domain, secure=secure_flag,
            httponly=httponly or False, samesite=samesite,
            expires='Thu, 01 Jan 1970 00:00:00 GMT',
        )
