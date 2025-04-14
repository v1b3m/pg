@@ -66,26 +66,24 @@ class Serializer(base.Serializer):
            if self.use_natural_foreign_keys and hasattr(
                field.remote_field.model, "natural_key"
            ):
                # Use natural key values for m2m
                m2m_iter = getattr(obj, "_prefetched_objects_cache", {}).get(
                    field.name,
                    getattr(obj, field.name).iterator(),
                )
                # For each related object, return its natural key
                self._current[field.name] = [related.natural_key() for related in m2m_iter]
            else:
                # Use primary key values for m2m
                prefetched = getattr(obj, "_prefetched_objects_cache", {}).get(field.name, None)
                if prefetched is not None:
                    # Prefetched objects are model instances
                    self._current[field.name] = [self._value_from_field(rel, rel._meta.pk) for rel in prefetched]
                else:
                    # Use values_list to retrieve only pk values efficiently
                    m2m_qs = getattr(obj, field.name).values_list("pk", flat=True)
                    m2m_iter = m2m_qs.iterator()
                    self._current[field.name] = list(m2m_iter)

    def getvalue(self):
        return self.objects