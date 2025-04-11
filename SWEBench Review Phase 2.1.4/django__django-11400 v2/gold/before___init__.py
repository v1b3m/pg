@@ -825,9 +825,11 @@ def get_choices(self, include_blank=True, blank_choice=BLANK_CHOICE_DASH, limit_
            if hasattr(self.remote_field, 'get_related_field')
            else 'pk'
        )
        return (blank_choice if include_blank else []) + [
            (choice_func(x), str(x))
            for x in rel_model._default_manager.complex_filter(limit_choices_to).order_by(*ordering)
        ]

    def value_to_string(self, obj):