@@ -1666,6 +1666,12 @@ class Query(BaseExpression):
            filter_expr = (filter_lhs, OuterRef(filter_rhs.name))
        # Generate the inner query.
        query = Query(self.model)
        query.add_filter(filter_expr)
        query.clear_ordering(True)
        # Try to have as simple as possible subquery -> trim leading joins from