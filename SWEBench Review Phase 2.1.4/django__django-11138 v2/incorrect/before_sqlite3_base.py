@@ -374,6 +374,119 @@ class DatabaseWrapper(BaseDatabaseWrapper):
    def is_in_memory_db(self):
        return self.creation.is_in_memory_db(self.settings_dict['NAME'])


FORMAT_QMARK_REGEX = re.compile(r'(?<!%)%s')
