@@ -591,6 +591,22 @@ class BookAdmin(ModelAdmin):
        expected = [(self.john.pk, 'John Blue'), (self.jack.pk, 'Jack Red')]
        self.assertEqual(filterspec.lookup_choices, expected)

    def test_relatedfieldlistfilter_manytomany(self):
        modeladmin = BookAdmin(Book, site)

@@ -696,6 +712,23 @@ def test_relatedfieldlistfilter_reverse_relationships(self):
        filterspec = changelist.get_filters(request)[0]
        self.assertEqual(len(filterspec), 0)

    def test_relatedonlyfieldlistfilter_foreignkey(self):
        modeladmin = BookAdminRelatedOnlyFilter(Book, site)

@@ -708,6 +741,57 @@ def test_relatedonlyfieldlistfilter_foreignkey(self):
        expected = [(self.alfred.pk, 'alfred'), (self.bob.pk, 'bob')]
        self.assertEqual(sorted(filterspec.lookup_choices), sorted(expected))

    def test_relatedonlyfieldlistfilter_underscorelookup_foreignkey(self):
        Department.objects.create(code='TEST', description='Testing')
        self.djangonaut_book.employee = self.john