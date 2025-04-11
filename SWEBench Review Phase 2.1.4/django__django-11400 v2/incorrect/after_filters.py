@@ -194,10 +194,16 @@ class RelatedFieldListFilter(FieldListFilter):
        return [self.lookup_kwarg, self.lookup_kwarg_isnull]

    def field_choices(self, field, request, model_admin):
        # Determine ordering for the related model's choices.
        related_model = field.remote_field.model
        related_admin = model_admin.admin_site._registry.get(related_model)
        if related_admin is not None:
            ordering = related_admin.get_ordering(request)
        else:
            ordering = None
        # If ordering is falsy (None or empty tuple/list), fall back to related model's Meta.ordering
        if not ordering:
            ordering = related_model._meta.ordering or ()
        return field.get_choices(include_blank=False, ordering=ordering)

    def choices(self, changelist):
@@ -418,5 +424,15 @@ FieldListFilter.register(lambda f: True, AllValuesFieldListFilter)

class RelatedOnlyFieldListFilter(RelatedFieldListFilter):
    def field_choices(self, field, request, model_admin):
        # Limit available choices to those related to the current model entries
        pk_qs = model_admin.get_queryset(request).distinct().values_list('%s__pk' % self.field_path, flat=True)
        # Determine ordering for related model
        related_model = field.remote_field.model
        related_admin = model_admin.admin_site._registry.get(related_model)
        if related_admin is not None:
            ordering = related_admin.get_ordering(request)
        else:
            ordering = None
        if not ordering:
            ordering = related_model._meta.ordering or ()
        return field.get_choices(include_blank=False, limit_choices_to={'pk__in': pk_qs}, ordering=ordering)