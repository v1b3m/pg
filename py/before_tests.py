            "custom base_name message",
        )

    def test_deconstruction(self):
        constraint = BaseConstraint(
            name="base_name",
            violation_error_message="custom %(name)s message",
        )
        path, args, kwargs = constraint.deconstruct()
        self.assertEqual(path, "django.db.models.BaseConstraint")
        self.assertEqual(args, ())
        self.assertEqual(
            kwargs,
            {"name": "base_name", "violation_error_message": "custom %(name)s message"},
        )

    def test_deprecation(self):
                check=check1, name="price", violation_error_message="custom error"
            ),
        )

    def test_repr(self):
        constraint = models.CheckConstraint(
            "violation_error_message='More than 1'>",
        )

    def test_invalid_check_types(self):
        msg = "CheckConstraint.check must be a Q instance or boolean expression."
        with self.assertRaisesMessage(TypeError, msg):
        # Valid product.
        constraint.validate(Product, Product(price=10, discounted_price=5))

    def test_validate_boolean_expressions(self):
        constraint = models.CheckConstraint(
            check=models.expressions.ExpressionWrapper(
                violation_error_message="custom error",
            ),
        )

    def test_eq_with_condition(self):
        self.assertEqual(
            ),
        )

    def test_deconstruction(self):
        fields = ["foo", "bar"]
        name = "unique_fields"

    def test_validate(self):
        constraint = UniqueConstraintProduct._meta.constraints[0]
        msg = "Unique constraint product with this Name and Color already exists."
        non_unique_product = UniqueConstraintProduct(
            name=self.p1.name, color=self.p1.color
        )
        with self.assertRaisesMessage(ValidationError, msg):
            constraint.validate(UniqueConstraintProduct, non_unique_product)
        # Null values are ignored.
        constraint.validate(
            UniqueConstraintProduct,
            exclude={"name"},
        )

    def test_validate_expression(self):
        constraint = models.UniqueConstraint(Lower("name"), name="name_lower_uniq")
        msg = "Constraint “name_lower_uniq” is violated."
diff --git a/tests/postgres_tests/test_constraints.py b/tests/postgres_tests/test_constraints.py