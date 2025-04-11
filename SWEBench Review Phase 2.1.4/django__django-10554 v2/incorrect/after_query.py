@@ -333,6 +333,9 @@ class Query(BaseExpression):
            del obj.base_table
        except AttributeError:
            pass
        # Clone combined_queries if present
        if self.combined_queries:
            obj.combined_queries = tuple(q.clone() for q in self.combined_queries)
        return obj

    def chain(self, klass=None):