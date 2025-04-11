@@ -122,8 +122,11 @@ def get_choices(self, include_blank=True, blank_choice=BLANK_CHOICE_DASH, orderi
        Analog of django.db.models.fields.Field.get_choices(), provided
        initially for utilization by RelatedFieldListFilter.
        """
        return (blank_choice if include_blank else []) + [
            (x.pk, str(x)) for x in self.related_model._default_manager.order_by(*ordering)
        ]

    def is_hidden(self):