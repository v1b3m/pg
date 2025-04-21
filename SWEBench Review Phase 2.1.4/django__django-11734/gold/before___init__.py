            value = connection.ops.validate_autopk_value(value)
        return value

    def get_prep_value(self, value):
        from django.db.models.expressions import OuterRef
        return value if isinstance(value, OuterRef) else super().get_prep_value(value)

    def contribute_to_class(self, cls, name, **kwargs):
        assert not cls._meta.auto_field, (
            "Model %s can't have more than one auto-generated field."