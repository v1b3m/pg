@@ -1705,22 +1705,30 @@ class Model(metaclass=ModelBase):
        # Check related fields.
        for field in related_fields:
            _cls = cls
            prev_fld = None
            for part in field.split(LOOKUP_SEP):
                if part == 'pk' and prev_fld is not None and prev_fld.is_relation:
                    fld = _cls._meta.pk
                else:
                    try:
                        fld = _cls._meta.get_field(part)
                    except (FieldDoesNotExist, AttributeError):
                        # If transform exists on the previous field, allow and continue
                        if prev_fld is not None and prev_fld.get_transform(part) is not None:
                            continue
                        # No transform available: add error and stop processing this field string
                        errors.append(
                            checks.Error(
                                "'ordering' refers to the nonexistent field, related field, or lookup '%s'." % field,
                                obj=cls,
                                id='models.E015',
                            )
                        )
                        break
                # Update current class and prev_fld
                if fld.is_relation:
                    _cls = fld.get_path_info()[-1].to_opts.model
                prev_fld = fld

        # Skip ordering on pk. This is always a valid order_by field
        # but is an alias and therefore won't be found by opts.get_field.