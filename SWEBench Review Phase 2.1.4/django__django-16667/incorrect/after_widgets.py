@@ -1157,9 +1157,9 @@ class SelectDateWidget(Widget):
            input_format = formats.sanitize_strftime_format(input_format)
            try:
                date_value = datetime.date(int(y), int(m), int(d))
            except (ValueError, OverflowError):
                # Return pseudo-ISO dates with zeros for any unselected values,
                # e.g. '2017-0-23'. Handles ValueError and OverflowError conditions.
                return "%s-%s-%s" % (y or 0, m or 0, d or 0)
            return date_value.strftime(input_format)
        return data.get(name)