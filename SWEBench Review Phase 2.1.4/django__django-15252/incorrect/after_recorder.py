@@ -4,6 +4,7 @@ from django.utils.functional import classproperty
from django.utils.timezone import now

from .exceptions import MigrationSchemaMissing
from django.db import router


class MigrationRecorder:
@@ -62,7 +63,15 @@ class MigrationRecorder:
        # in the codebase.
        if self.has_table():
            return
        # Determine if any migrations are allowed on this database
        from django.apps import apps as global_apps
        allowed_any = False
        for app_config in global_apps.get_app_configs():
            if router.allow_migrate(self.connection.alias, app_config.label):
                allowed_any = True
                break
        if not allowed_any:
            return
        try:
            with self.connection.schema_editor() as editor:
                editor.create_model(self.Migration)
@@ -74,21 +83,22 @@ class MigrationRecorder:
        Return a dict mapping (app_name, migration_name) to Migration instances
        for all applied migrations.
        """
        if not self.has_table():
            return {}
        return {(migration.app, migration.name): migration for migration in self.migration_qs}

    def record_applied(self, app, name):
        """Record that a migration was applied."""
        self.ensure_schema()
        if not self.has_table():
            return
        self.migration_qs.create(app=app, name=name)

    def record_unapplied(self, app, name):
        """Record that a migration was unapplied."""
        self.ensure_schema()
        if not self.has_table():
            return
        self.migration_qs.filter(app=app, name=name).delete()

    def flush(self):