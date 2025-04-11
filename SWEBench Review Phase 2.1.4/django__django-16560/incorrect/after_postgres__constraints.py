@@ -33,6 +33,7 @@ class ExclusionConstraint(BaseConstraint):
        deferrable=None,
        include=None,
        violation_error_message=None,
        violation_error_code=None,
    ):
        if index_type and index_type.lower() not in {"gist", "spgist"}:
            raise ValueError(
@@ -60,7 +61,7 @@ class ExclusionConstraint(BaseConstraint):
        self.condition = condition
        self.deferrable = deferrable
        self.include = tuple(include) if include else ()
        super().__init__(name=name, violation_error_message=violation_error_message, violation_error_code=violation_error_code)

    def _get_expressions(self, schema_editor, query):
        expressions = []
@@ -150,11 +151,12 @@ class ExclusionConstraint(BaseConstraint):
                and self.deferrable == other.deferrable
                and self.include == other.include
                and self.violation_error_message == other.violation_error_message
                and getattr(self, 'violation_error_code', None) == getattr(other, 'violation_error_code', None)
            )
        return super().__eq__(other)

    def __repr__(self):
        return "<%s: index_type=%s expressions=%s name=%s%s%s%s%s%s>" % (
            self.__class__.__qualname__,
            repr(self.index_type),
            repr(self.expressions),
@@ -164,9 +166,11 @@ class ExclusionConstraint(BaseConstraint):
            "" if not self.include else " include=%s" % repr(self.include),
            (
                ""
                if self.violation_error_message is None or self.violation_error_message == self.default_violation_error_message
                else " violation_error_message=%r" % self.violation_error_message
            ) + (
                ""
                if getattr(self, 'violation_error_code', None) is None else " violation_error_code=%r" % self.violation_error_code
            ),
        )

@@ -204,9 +208,9 @@ class ExclusionConstraint(BaseConstraint):
            queryset = queryset.exclude(pk=model_class_pk)
        if not self.condition:
            if queryset.exists():
                raise ValidationError(self.get_violation_error_message(), code=self.violation_error_code)
        else:
            if (self.condition & Exists(queryset.filter(self.condition))).check(
                replacement_map, using=using
            ):
                raise ValidationError(self.get_violation_error_message(), code=self.violation_error_code)