@@ -232,9 +232,14 @@ class Collector:
        """
        Get a QuerySet of objects related to `objs` via the relation `related`.
        """
        qs = related.related_model._base_manager.using(self.using).filter(
            **{"%s__in" % related.field.name: objs}
        )
        # Only select primary key and required foreign key fields for related objects
        foreign_field_names = [f.name for f in related.related_model._meta.concrete_fields if f.remote_field is not None and not f.many_to_many]
        if 'pk' not in foreign_field_names:
            foreign_field_names.insert(0, 'pk')
        return qs.only(*foreign_field_names)

    def instances_with_model(self):
        for model, instances in self.data.items():
diff --git a/django/db/models/query.py b/django/db/models/query.py
index 84236107f3..4efe5a3d70 100644
++ b/django/db/models/query.py
@@ -695,6 +695,13 @@ class QuerySet:
        del_query.query.select_related = False
        del_query.query.clear_ordering(force_empty=True)

        # Restrict deletion query to only load primary key and required foreign keys
        # Determine foreign key field names
        foreign_field_names = [f.name for f in del_query.model._meta.concrete_fields if f.remote_field is not None and not f.many_to_many]
        if 'pk' not in foreign_field_names:
            # include pk explicitly
            foreign_field_names.insert(0, 'pk')
        del_query = del_query.only(*foreign_field_names)
        collector = Collector(using=del_query.db)
        collector.collect(del_query)
        deleted, _rows_count = collector.delete()