@@ -1297,26 +1297,31 @@ class Model(metaclass=ModelBase):

    @classmethod
    def _check_default_pk(cls):
        # Skip warning for auto-created one-to-one parent link if the parent has a manually defined primary key.
        from django.db.models.fields.related import OneToOneField
        pk_field = cls._meta.pk
        if pk_field.auto_created:
            # If it's an auto-created one-to-one link and parent pk not auto_created, skip warning.
            if isinstance(pk_field, OneToOneField) and getattr(pk_field.remote_field, 'parent_link', False):
                parent_model = pk_field.remote_field.model
                if parent_model is not None and not parent_model._meta.pk.auto_created:
                    return []
            if not settings.is_overridden('DEFAULT_AUTO_FIELD') and not cls._meta.app_config._is_default_auto_field_overridden:
                return [
                    checks.Warning(
                        f"Auto-created primary key used when not defining a "
                        f"primary key type, by default "
                        f"'{settings.DEFAULT_AUTO_FIELD}'.",
                        hint=(
                            f"Configure the DEFAULT_AUTO_FIELD setting or the "
                            f"{cls._meta.app_config.__class__.__qualname__}."
                            f"default_auto_field attribute to point to a subclass "
                            f"of AutoField, e.g. 'django.db.models.BigAutoField'."
                        ),
                        obj=cls,
                        id='models.W042',
                    ),
                ]
        return []

    @classmethod