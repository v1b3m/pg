    def reduce(self, operation, app_label):
        return (
            super().reduce(operation, app_label) or
            not operation.references_model(self.name, app_label)
        )


class CreateModel(ModelOperation):
    """Create a model's table."""
    def migration_name_fragment(self):
        return 'alter_%s_%s' % (self.name_lower, self.option_name)


class AlterUniqueTogether(AlterTogetherOptionOperation):
    """