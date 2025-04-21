@@ -1185,7 +1185,10 @@ class ModelChoiceField(ChoiceField):
                 required=True, widget=None, label=None, initial=None,
                 help_text='', to_field_name=None, limit_choices_to=None,
                 **kwargs):
        # If field is required and initial not provided, normally would include empty_label
        # But if widget is RadioSelect (or subclass), treat differently (avoid empty choice)
        from django.forms import widgets as form_widgets
        if required and (initial is not None or (widget is not None and isinstance(widget, form_widgets.RadioSelect))):
            self.empty_label = None
        else:
            self.empty_label = empty_label