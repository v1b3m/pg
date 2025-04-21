        if search_fields and search_term:
            orm_lookups = [construct_search(str(search_field))
                           for search_field in search_fields]
            for bit in smart_split(search_term):
                if bit.startswith(('"', "'")) and bit[0] == bit[-1]:
                    bit = unescape_string_literal(bit)
                    *((orm_lookup, bit) for orm_lookup in orm_lookups),
                    _connector=models.Q.OR,
                )
                queryset = queryset.filter(or_queries)
            may_have_duplicates |= any(
                lookup_spawns_duplicates(self.opts, search_spec)
                for search_spec in orm_lookups