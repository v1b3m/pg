class SubThingInline(admin.StackedInline):
    model = SubThing


@admin.register(Thing)
class ThingAdmin(admin.ModelAdmin):
    list_display = ("name",)
    ordering = ("pkid",)
    inlines = (SubThingInline,)
