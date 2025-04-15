@@ -309,8 +309,15 @@ class Collector:
                        sender=model, instance=obj, using=self.using
                    )

            # fast deletes, combine by model
            fast_deletes_by_model = {}
            for qs in self.fast_deletes:
                if qs.model in fast_deletes_by_model:
                    # combine queries using OR
                    fast_deletes_by_model[qs.model] = fast_deletes_by_model[qs.model] | qs
                else:
                    fast_deletes_by_model[qs.model] = qs
            for qs in fast_deletes_by_model.values():
                count = qs._raw_delete(using=self.using)
                deleted_counter[qs.model._meta.label] += count
