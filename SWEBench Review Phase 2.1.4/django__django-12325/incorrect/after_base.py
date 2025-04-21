@@ -204,7 +204,19 @@ class ModelBase(type):
            for field in base._meta.local_fields:
                if isinstance(field, OneToOneField):
                    related = resolve_relation(new_class, field.remote_field.model)
                    key = make_model_tuple(related)
                    existing_field = parent_links.get(key)
                    if existing_field is None:
                        parent_links[key] = field
                    else:
                        if field.remote_field.parent_link and not getattr(existing_field.remote_field, 'parent_link', False):
                            parent_links[key] = field
                        elif getattr(existing_field.remote_field, 'parent_link', False):
                            # Existing is a parent link, prefer it over non-parent_link fields
                            continue
                        else:
                            # Neither existing nor current are marked as parent_link: override with last defined
                            parent_links[key] = field

        # Track fields inherited from base models.
        inherited_attributes = set()