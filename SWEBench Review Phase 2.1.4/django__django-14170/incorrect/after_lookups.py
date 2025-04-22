@@ -548,10 +548,9 @@ class YearLookup(Lookup):

    def as_sql(self, compiler, connection):
        # Avoid the extract operation if the rhs is a direct value to allow
        # indexes to be used, except for iso_year lookup.
        if self.rhs_is_direct_value() and getattr(self.lhs, 'lookup_name', None) != 'iso_year':
            # Skip the extract part by directly using the originating field, that is self.lhs.lhs.
            lhs_sql, params = self.process_lhs(compiler, connection, self.lhs.lhs)
            rhs_sql, _ = self.process_rhs(compiler, connection)
            rhs_sql = self.get_direct_rhs_sql(connection, rhs_sql)