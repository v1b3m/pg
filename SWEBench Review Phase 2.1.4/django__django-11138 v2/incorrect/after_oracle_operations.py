@@ -99,9 +99,12 @@ END;
            return field_name
        if not self._tzname_re.match(tzname):
            raise ValueError("Invalid time zone name: %s" % tzname)
        # Convert from connection time zone to target tz
        # If tzname equals connection.timezone_name, no conversion needed
        from_tz = self.connection.timezone_name
        if tzname == from_tz:
            return field_name
        return "CAST((FROM_TZ(%s, '%s') AT TIME ZONE '%s') AS TIMESTAMP)" % (field_name, from_tz, tzname)

    def datetime_cast_date_sql(self, field_name, tzname):
        field_name = self._convert_field_to_tz(field_name, tzname)