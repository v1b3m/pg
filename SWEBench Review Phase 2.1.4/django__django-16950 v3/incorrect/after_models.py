@@ -1172,7 +1172,8 @@ class BaseInlineFormSet(BaseModelFormSet):

        # If we're adding a new object, ignore a parent's auto-generated key
        # as it will be regenerated on the save request.
        if self.instance._state.adding and not form.is_bound:
            # For initial, ignore any parent's auto-generated default key
            if kwargs.get("to_field") is not None:
                to_field = self.instance._meta.get_field(kwargs["to_field"])
            else: