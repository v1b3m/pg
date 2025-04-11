@@ -70,7 +70,11 @@ class DatabaseOperations(BaseDatabaseOperations):

    def _convert_field_to_tz(self, field_name, tzname):
        if settings.USE_TZ:
            field_name = "CONVERT_TZ(%s, 'UTC', '%s')" % (field_name, tzname)
        return field_name

    def datetime_cast_date_sql(self, field_name, tzname):