@@ -727,7 +727,7 @@ class SQLCompiler:
        # If we get to this point and the field is a relation to another model,
        # append the default ordering for that model unless it is the pk
        # shortcut or the attribute name of the field that is specified.
        if field.is_relation and opts.ordering and getattr(field, 'attname', None) != name and name != 'pk' and len(pieces) == 1:
            # Firstly, avoid infinite loops.
            already_seen = already_seen or set()
            join_tuple = tuple(getattr(self.query.alias_map[j], 'join_cols', None) for j in joins)