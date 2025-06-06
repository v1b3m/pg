@@ -431,6 +431,13 @@ class Model(metaclass=ModelBase):
            for val, field in zip(args, fields_iter):
                if val is _DEFERRED:
                    continue
                # Convert enum values to underlying value
                try:
                    import enum as _enum
                except ImportError:
                    _enum = None
                if _enum is not None and isinstance(val, _enum.Enum):
                    val = val.value
                _setattr(self, field.attname, val)
        else:
            # Slower, kwargs-ready version.
@@ -438,6 +445,12 @@ class Model(metaclass=ModelBase):
            for val, field in zip(args, fields_iter):
                if val is _DEFERRED:
                    continue
                try:
                    import enum as _enum
                except ImportError:
                    _enum = None
                if _enum is not None and isinstance(val, _enum.Enum):
                    val = val.value
                _setattr(self, field.attname, val)
                kwargs.pop(field.name, None)

@@ -482,6 +495,13 @@ class Model(metaclass=ModelBase):
                    _setattr(self, field.name, rel_obj)
            else:
                if val is not _DEFERRED:
                    # Convert enum values to underlying value
                    try:
                        import enum as _enum
                    except ImportError:
                        _enum = None
                    if _enum is not None and isinstance(val, _enum.Enum):
                        val = val.value
                    _setattr(self, field.attname, val)

        if kwargs: