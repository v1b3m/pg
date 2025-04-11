@@ -19,10 +19,11 @@ __all__ = ["BaseConstraint", "CheckConstraint", "Deferrable", "UniqueConstraint"
class BaseConstraint:
    default_violation_error_message = _("Constraint “%(name)s” is violated.")
    violation_error_message = None
    violation_error_code = None

    # RemovedInDjango60Warning: When the deprecation ends, replace with:
    # def __init__(self, *, name, violation_error_message=None):
    def __init__(self, *args, name=None, violation_error_message=None, violation_error_code=None):
        # RemovedInDjango60Warning.
        if name is None and not args:
            raise TypeError(
@@ -34,6 +35,7 @@ class BaseConstraint:
            self.violation_error_message = violation_error_message
        else:
            self.violation_error_message = self.default_violation_error_message
        self.violation_error_code = violation_error_code
        # RemovedInDjango60Warning.
        if args:
            warnings.warn(
@@ -74,6 +76,8 @@ class BaseConstraint:
            and self.violation_error_message != self.default_violation_error_message
        ):
            kwargs["violation_error_message"] = self.violation_error_message
        if getattr(self, 'violation_error_code', None) is not None:
            kwargs['violation_error_code'] = self.violation_error_code
        return (path, (), kwargs)

    def clone(self):
@@ -82,13 +86,13 @@ class BaseConstraint:


class CheckConstraint(BaseConstraint):
    def __init__(self, *, check, name, violation_error_message=None, violation_error_code=None):
        self.check = check
        if not getattr(check, "conditional", False):
            raise TypeError(
                "CheckConstraint.check must be a Q instance or boolean expression."
            )
        super().__init__(name=name, violation_error_message=violation_error_message, violation_error_code=violation_error_code)

    def _get_check_sql(self, model, schema_editor):
        query = Query(model=model, alias_cols=False)
@@ -112,7 +116,7 @@ class CheckConstraint(BaseConstraint):
        against = instance._get_field_value_map(meta=model._meta, exclude=exclude)
        try:
            if not Q(self.check).check(against, using=using):
                raise ValidationError(self.get_violation_error_message(), code=self.violation_error_code)
        except FieldError:
            pass

@@ -123,9 +127,12 @@ class CheckConstraint(BaseConstraint):
            repr(self.name),
            (
                ""
                if self.violation_error_message is None or self.violation_error_message == self.default_violation_error_message
                else " violation_error_message=%r" % self.violation_error_message
            ) + (
                ""
                if getattr(self, 'violation_error_code', None) is None
                else " violation_error_code=%r" % self.violation_error_code
            ),
        )

@@ -164,6 +171,7 @@ class UniqueConstraint(BaseConstraint):
        include=None,
        opclasses=(),
        violation_error_message=None,
        violation_error_code=None,
    ):
        if not name:
            raise ValueError("A unique constraint must be named.")
@@ -213,7 +221,7 @@ class UniqueConstraint(BaseConstraint):
            F(expression) if isinstance(expression, str) else expression
            for expression in expressions
        )
        super().__init__(name=name, violation_error_message=violation_error_message, violation_error_code=violation_error_code)

    @property
    def contains_expressions(self):
@@ -304,9 +312,13 @@ class UniqueConstraint(BaseConstraint):
            "" if not self.opclasses else " opclasses=%s" % repr(self.opclasses),
            (
                ""
                if self.violation_error_message is None or self.violation_error_message == self.default_violation_error_message
                else " violation_error_message=%r" % self.violation_error_message
            )
            + (
                ""
                if getattr(self, 'violation_error_code', None) is None
                else " violation_error_code=%r" % self.violation_error_code
            ),
        )

@@ -321,6 +333,7 @@ class UniqueConstraint(BaseConstraint):
                and self.opclasses == other.opclasses
                and self.expressions == other.expressions
                and self.violation_error_message == other.violation_error_message
                and getattr(self, 'violation_error_code', None) == getattr(other, 'violation_error_code', None)
            )
        return super().__eq__(other)

@@ -385,7 +398,7 @@ class UniqueConstraint(BaseConstraint):
        if not self.condition:
            if queryset.exists():
                if self.expressions:
                    raise ValidationError(self.get_violation_error_message(), code=self.violation_error_code)
                # When fields are defined, use the unique_error_message() for
                # backward compatibility.
                for model, constraints in instance.get_constraints():
@@ -400,6 +413,6 @@ class UniqueConstraint(BaseConstraint):
                if (self.condition & Exists(queryset.filter(self.condition))).check(
                    against, using=using
                ):
                    raise ValidationError(self.get_violation_error_message(), code=self.violation_error_code)
            except FieldError:
                pass