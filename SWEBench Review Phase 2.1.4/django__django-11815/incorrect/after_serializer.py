@@ -120,6 +120,13 @@ class EnumSerializer(BaseSerializer):
    def serialize(self):
        enum_class = self.value.__class__
        module = enum_class.__module__
        # If the enum value is a lazy translation (Promise), use enum name instead to avoid translation issues.
        from django.utils.functional import Promise, LazyObject
        if isinstance(self.value.value, Promise) or isinstance(self.value.value, LazyObject):
            imports = {f"import {module}"}
            # Represent as EnumClass['NAME']
            return "%s.%s['%s']" % (module, enum_class.__name__, self.value.name), imports
        # Otherwise, represent using its value
        v_string, v_imports = serializer_factory(self.value.value).serialize()
        imports = {'import %s' % module, *v_imports}
        return "%s.%s(%s)" % (module, enum_class.__name__, v_string), imports