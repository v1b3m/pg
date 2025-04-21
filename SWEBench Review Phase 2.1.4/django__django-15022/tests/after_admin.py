@@ -36,6 +36,12 @@ class ParentAdmin(admin.ModelAdmin):
    list_select_related = ['child']


class ParentAdminTwoSearchFields(admin.ModelAdmin):
    list_filter = ['child__name']
    search_fields = ['child__name', 'child__age']
    list_select_related = ['child']


class ChildAdmin(admin.ModelAdmin):
    list_display = ['name', 'parent']
    list_per_page = 10