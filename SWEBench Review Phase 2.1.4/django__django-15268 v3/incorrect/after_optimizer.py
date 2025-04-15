@@ -41,6 +41,18 @@ class MigrationOptimizer:
        """Inner optimization loop."""
        new_operations = []
        for i, operation in enumerate(operations):
            # Check for pattern of AlterFooTogether removals followed by additions
            from django.db.migrations.operations import models as model_ops
            if (isinstance(operation, model_ops.AlterUniqueTogether) and not operation.option_value and
                    i + 3 < len(operations) and isinstance(operations[i+1], model_ops.AlterIndexTogether) and not operations[i+1].option_value and
                    isinstance(operations[i+2], model_ops.AlterUniqueTogether) and operations[i+2].option_value and
                    isinstance(operations[i+3], model_ops.AlterIndexTogether) and operations[i+3].option_value and
                    operation.name_lower == operations[i+1].name_lower == operations[i+2].name_lower == operations[i+3].name_lower and
                    all(not op.references_model(operation.name, app_label) for op in new_operations)):
                # Optimize by dropping removal ops and keeping only addition ops
                new_operations.extend(operations[i+2:i+4])
                new_operations.extend(operations[i+4:])
                return new_operations
            right = True  # Should we reduce on the right or on the left.
            # Compare it to each operation after it
            for j, other in enumerate(operations[i + 1:]):