@@ -134,20 +134,25 @@ class SplitArrayWidget(forms.Widget):
        attrs = {} if attrs is None else attrs
        context = super().get_context(name, value, attrs)
        if self.is_localized:
            # Ensure the base widget inherits localization settings.
            self.widget.is_localized = self.is_localized
        value = value or []
        context['widget']['subwidgets'] = []
        # Build base attributes from provided attrs
        base_attrs = self.build_attrs(attrs)
        id_ = base_attrs.get('id')
        for i in range(max(len(value), self.size)):
            try:
                widget_value = value[i]
            except IndexError:
                widget_value = None
            # Copy base_attrs for each subwidget, then update id if present
            sub_attrs = base_attrs.copy()
            if id_:
                sub_attrs['id'] = '%s_%s' % (id_, i)
            # Get context for the widget with its own attributes
            context['widget']['subwidgets'].append(
                self.widget.get_context(name + '_%s' % i, widget_value, sub_attrs)['widget']
            )
        return context
