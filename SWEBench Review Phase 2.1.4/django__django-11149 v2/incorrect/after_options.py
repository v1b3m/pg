@@ -2113,29 +2113,33 @@ class InlineModelAdmin(BaseModelAdmin):

    def has_add_permission(self, request, obj):
        if self.opts.auto_created:
            # For auto-created intermediate models, require change permission on the parent model.
            parent_admin = self.admin_site._registry.get(self.parent_model)
            if parent_admin is not None:
                return parent_admin.has_change_permission(request, obj)
            # Fallback to default permission check on parent model
            parent_opts = self.parent_model._meta
            return request.user.has_perm('%s.%s' % (parent_opts.app_label, get_permission_codename('change', parent_opts)))
        return super().has_add_permission(request)

    def has_change_permission(self, request, obj=None):
        if self.opts.auto_created:
            # For auto-created intermediate models, require change permission on the parent model.
            parent_admin = self.admin_site._registry.get(self.parent_model)
            if parent_admin is not None:
                return parent_admin.has_change_permission(request, obj)
            parent_opts = self.parent_model._meta
            return request.user.has_perm('%s.%s' % (parent_opts.app_label, get_permission_codename('change', parent_opts)))
        return super().has_change_permission(request)

    def has_delete_permission(self, request, obj=None):
        if self.opts.auto_created:
            # For auto-created intermediate models, require change permission on the parent model.
            parent_admin = self.admin_site._registry.get(self.parent_model)
            if parent_admin is not None:
                return parent_admin.has_change_permission(request, obj)
            parent_opts = self.parent_model._meta
            return request.user.has_perm('%s.%s' % (parent_opts.app_label, get_permission_codename('change', parent_opts)))
        return super().has_delete_permission(request, obj)

    def has_view_permission(self, request, obj=None):