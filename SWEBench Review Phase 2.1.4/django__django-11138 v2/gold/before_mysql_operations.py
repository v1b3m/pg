@@ -84,27 +84,29 @@ def date_trunc_sql(self, lookup_type, field_name):
    def time_trunc_sql(self, lookup_type, field_name):
        return "django_time_trunc('%s', %s)" % (lookup_type.lower(), field_name)

    def _convert_tzname_to_sql(self, tzname):
        return "'%s'" % tzname if settings.USE_TZ else 'NULL'

    def datetime_cast_date_sql(self, field_name, tzname):
        return "django_datetime_cast_date(%s, %s)" % (
            field_name, self._convert_tzname_to_sql(tzname),
        )

    def datetime_cast_time_sql(self, field_name, tzname):
        return "django_datetime_cast_time(%s, %s)" % (
            field_name, self._convert_tzname_to_sql(tzname),
        )

    def datetime_extract_sql(self, lookup_type, field_name, tzname):
        return "django_datetime_extract('%s', %s, %s)" % (
            lookup_type.lower(), field_name, self._convert_tzname_to_sql(tzname),
        )

    def datetime_trunc_sql(self, lookup_type, field_name, tzname):
        return "django_datetime_trunc('%s', %s, %s)" % (
            lookup_type.lower(), field_name, self._convert_tzname_to_sql(tzname),
        )

    def time_extract_sql(self, lookup_type, field_name):