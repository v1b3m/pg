@@ -803,10 +803,12 @@ class Model(metaclass=ModelBase):
        meta = cls._meta
        inserted = False
        for parent, field in meta.parents.items():
            # Make sure the link fields are synced appropriately between parent and self.
            if field and getattr(self, parent._meta.pk.attname) is None:
                # Only propagate existing pointer value to parent pk if this instance is being added with an existing parent pointer.
                if getattr(self, field.attname) is not None and self._state.adding:
                    setattr(self, parent._meta.pk.attname, getattr(self, field.attname))
                # If instance is not adding and parent pk is None, leave parent pk None to create a new parent.
            parent_inserted = self._save_parents(cls=parent, using=using, update_fields=update_fields)
            updated = self._save_table(
                cls=parent, using=using, update_fields=update_fields,