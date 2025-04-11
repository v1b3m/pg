@@ -1666,6 +1666,12 @@ class Query(BaseExpression):
            filter_expr = (filter_lhs, OuterRef(filter_rhs.name))
        # Generate the inner query.
        query = Query(self.model)
        # Propagate any FilteredRelation annotations to the inner query, if present.
        if self._filtered_relations:
            # Clone each FilteredRelation object for the new query.
            query._filtered_relations = {
                alias: fr.clone() for alias, fr in self._filtered_relations.items()
            }
        query.add_filter(filter_expr)
        query.clear_ordering(True)
        # Try to have as simple as possible subquery -> trim leading joins from