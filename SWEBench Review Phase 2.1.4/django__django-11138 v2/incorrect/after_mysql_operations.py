@@ -70,7 +70,11 @@ class DatabaseOperations(BaseDatabaseOperations):

    def _convert_field_to_tz(self, field_name, tzname):
        if settings.USE_TZ:
            from_tz = self.connection.timezone_name
            # If destination tz equals database tz, no conversion needed
            if tzname == from_tz:
                return field_name
            return "CONVERT_TZ(%s, '%s', '%s')" % (field_name, from_tz, tzname)
        return field_name

    def datetime_cast_date_sql(self, field_name, tzname):