@@ -374,6 +374,119 @@ class DatabaseWrapper(BaseDatabaseWrapper):
    def is_in_memory_db(self):
        return self.creation.is_in_memory_db(self.settings_dict['NAME'])

    def _sqlite_datetime_parse(self, dt, tzname=None):
        print('DEBUG instance _sqlite_datetime_parse', dt, type(dt), tzname)
        if dt is None:
            return None
        try:
            from django.utils.dateparse import parse_datetime
            parsed = parse_datetime(dt) if isinstance(dt, str) or isinstance(dt, bytes) else dt
        except Exception as e:
            print('Parse exc', e)
            parsed = None
        if parsed is None:
            try:
                parsed = backend_utils.typecast_timestamp(dt)
            except Exception as e:
                print('Typecast exc', e)
                parsed = None
        if parsed is None:
            return None
        # If value is naive and USE_TZ True, treat as connection.timezone
        if settings.USE_TZ and not timezone.is_aware(parsed):
            parsed = timezone.make_aware(parsed, self.timezone)
        # If tzname target provided, convert to that tz
        if tzname is not None:
            parsed = timezone.localtime(parsed, pytz.timezone(tzname))
        return parsed

    def _sqlite_date_trunc(self, lookup_type, dt):
        dt_obj = self._sqlite_datetime_parse(dt)
        if dt_obj is None:
            return None
        if lookup_type == 'year':
            return "%i-01-01" % dt_obj.year
        elif lookup_type == 'quarter':
            month_in_quarter = dt_obj.month - ((dt_obj.month - 1) % 3)
            return '%i-%02i-01' % (dt_obj.year, month_in_quarter)
        elif lookup_type == 'month':
            return "%i-%02i-01" % (dt_obj.year, dt_obj.month)
        elif lookup_type == 'week':
            dt_start = dt_obj - datetime.timedelta(days=dt_obj.weekday())
            return "%i-%02i-%02i" % (dt_start.year, dt_start.month, dt_start.day)
        elif lookup_type == 'day':
            return "%i-%02i-%02i" % (dt_obj.year, dt_obj.month, dt_obj.day)
        else:
            return None

    def _sqlite_date_extract(self, lookup_type, dt):
        print('DEBUG _sqlite_date_extract', lookup_type, dt)
        dt_obj = self._sqlite_datetime_parse(dt)
        if dt_obj is None:
            return None
        if lookup_type == 'week_day':
            return (dt_obj.isoweekday() % 7) + 1
        elif lookup_type == 'week':
            return dt_obj.isocalendar()[1]
        elif lookup_type == 'quarter':
            return math.ceil(dt_obj.month / 3)
        elif lookup_type == 'iso_year':
            return dt_obj.isocalendar()[0]
        else:
            return getattr(dt_obj, lookup_type)

    def _sqlite_datetime_cast_date(self, dt, tzname):
        dt_obj = self._sqlite_datetime_parse(dt, tzname)
        if dt_obj is None:
            return None
        return dt_obj.date().isoformat()

    def _sqlite_datetime_cast_time(self, dt, tzname):
        dt_obj = self._sqlite_datetime_parse(dt, tzname)
        if dt_obj is None:
            return None
        return dt_obj.time().isoformat()

    def _sqlite_datetime_extract(self, lookup_type, dt, tzname=None):
        dt_obj = self._sqlite_datetime_parse(dt, tzname)
        if dt_obj is None:
            return None
        if lookup_type == 'week_day':
            return (dt_obj.isoweekday() % 7) + 1
        elif lookup_type == 'week':
            return dt_obj.isocalendar()[1]
        elif lookup_type == 'quarter':
            return math.ceil(dt_obj.month / 3)
        elif lookup_type == 'iso_year':
            return dt_obj.isocalendar()[0]
        else:
            return getattr(dt_obj, lookup_type)

    def _sqlite_datetime_trunc(self, lookup_type, dt, tzname):
        dt_obj = self._sqlite_datetime_parse(dt, tzname)
        if dt_obj is None:
            return None
        if lookup_type == 'year':
            return "%i-01-01 00:00:00" % dt_obj.year
        elif lookup_type == 'quarter':
            month_in_quarter = dt_obj.month - ((dt_obj.month - 1) % 3)
            return '%i-%02i-01 00:00:00' % (dt_obj.year, month_in_quarter)
        elif lookup_type == 'month':
            return "%i-%02i-01 00:00:00" % (dt_obj.year, dt_obj.month)
        elif lookup_type == 'week':
            dt_start = dt_obj - datetime.timedelta(days=dt_obj.weekday())
            return "%i-%02i-%02i 00:00:00" % (dt_start.year, dt_start.month, dt_start.day)
        elif lookup_type == 'day':
            return "%i-%02i-%02i 00:00:00" % (dt_obj.year, dt_obj.month, dt_obj.day)
        elif lookup_type == 'hour':
            return "%i-%02i-%02i %02i:00:00" % (dt_obj.year, dt_obj.month, dt_obj.day, dt_obj.hour)
        elif lookup_type == 'minute':
            return "%i-%02i-%02i %02i:%02i:00" % (dt_obj.year, dt_obj.month, dt_obj.day, dt_obj.hour, dt_obj.minute)
        elif lookup_type == 'second':
            return "%i-%02i-%02i %02i:%02i:%02i" % (dt_obj.year, dt_obj.month, dt_obj.day, dt_obj.hour, dt_obj.minute, dt_obj.second)
        else:
            return None


FORMAT_QMARK_REGEX = re.compile(r'(?<!%)%s')
