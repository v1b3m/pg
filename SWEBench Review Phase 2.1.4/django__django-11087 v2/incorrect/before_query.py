@@ -232,9 +232,14 @@ class Collector:
        """
        Get a QuerySet of objects related to `objs` via the relation `related`.
        """
        return related.related_model._base_manager.using(self.using).filter(
            **{"%s__in" % related.field.name: objs}
        )

    def instances_with_model(self):
        for model, instances in self.data.items():
diff --git a/django/db/models/query.py b/django/db/models/query.py
index 84236107f3..4efe5a3d70 100644
-- a/django/db/models/query.py
@@ -695,6 +695,13 @@ class QuerySet:
        del_query.query.select_related = False
        del_query.query.clear_ordering(force_empty=True)

        collector = Collector(using=del_query.db)
        collector.collect(del_query)
        deleted, _rows_count = collector.delete()