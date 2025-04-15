            raise ValidationError(self.error_messages['invalid'], code='invalid')
        return value

    def validate(self, value):
        super().validate(value)
        if value in self.empty_values:
            return
        if not value.is_finite():
            raise ValidationError(self.error_messages['invalid'], code='invalid')

    def widget_attrs(self, widget):
        attrs = super().widget_attrs(widget)
        if isinstance(widget, NumberInput) and 'step' not in widget.attrs: