                # Return pseudo-ISO dates with zeros for any unselected values,
                # e.g. '2017-0-23'.
                return "%s-%s-%s" % (y or 0, m or 0, d or 0)
            return date_value.strftime(input_format)
        return data.get(name)
