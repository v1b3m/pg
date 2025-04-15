@@ -919,26 +919,22 @@ class Model(metaclass=ModelBase):
                obj = getattr(self, field.name, None)
                if not obj:
                    continue
                # A pk may have been assigned manually to a model instance not saved
                # to the database (or auto-generated in a case like UUIDField), but
                # allow the save to proceed and rely on the database to raise an
                # IntegrityError if applicable. If constraints aren't supported,
                # there's the risk of data corruption.
                if obj.pk is None:
                    if not field.remote_field.multiple:
                        field.remote_field.delete_cached_value(obj)
                    raise ValueError(
                        "%s() prohibited to prevent data loss due to unsaved related object '%s'." % (operation_name, field.name)
                    )
                # If the parent's attname value is still an automatically assigned default,
                # replace it with the related object's pk.
                if getattr(self, field.attname) is None or getattr(self, field.attname) is field.get_default():
                    setattr(self, field.attname, obj.pk)
                # If the relationship's pk/to_field was changed, clear the cached relationship.
                if getattr(obj, field.target_field.attname) != getattr(self, field.attname):
                    field.delete_cached_value(self)
