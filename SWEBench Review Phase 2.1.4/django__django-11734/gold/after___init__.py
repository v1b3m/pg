@@ -2332,10 +2332,6 @@ def get_db_prep_value(self, value, connection, prepared=False):
            value = connection.ops.validate_autopk_value(value)
        return value

    def contribute_to_class(self, cls, name, **kwargs):
        assert not cls._meta.auto_field, (
            "Model %s can't have more than one auto-generated field."