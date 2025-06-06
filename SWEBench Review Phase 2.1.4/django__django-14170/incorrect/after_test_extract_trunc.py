@@ -108,20 +108,32 @@ class DateFunctionTests(TestCase):
                qs = DTModel.objects.filter(**{'start_datetime__%s__exact' % lookup: 2015})
                self.assertEqual(qs.count(), 1)
                query_string = str(qs.query).lower()
                if lookup == 'iso_year':
                    self.assertEqual(query_string.count(' between '), 0)
                    self.assertGreaterEqual(query_string.count('extract'), 1)
                else:
                    self.assertEqual(query_string.count(' between '), 1)
                    self.assertEqual(query_string.count('extract'), 0)
                # exact is implied and should be the same
                qs = DTModel.objects.filter(**{'start_datetime__%s' % lookup: 2015})
                self.assertEqual(qs.count(), 1)
                query_string = str(qs.query).lower()
                if lookup == 'iso_year':
                    self.assertEqual(query_string.count(' between '), 0)
                    self.assertGreaterEqual(query_string.count('extract'), 1)
                else:
                    self.assertEqual(query_string.count(' between '), 1)
                    self.assertEqual(query_string.count('extract'), 0)
                # date and datetime fields should behave the same
                qs = DTModel.objects.filter(**{'start_date__%s' % lookup: 2015})
                self.assertEqual(qs.count(), 1)
                query_string = str(qs.query).lower()
                if lookup == 'iso_year':
                    self.assertEqual(query_string.count(' between '), 0)
                    self.assertGreaterEqual(query_string.count('extract'), 1)
                else:
                    self.assertEqual(query_string.count(' between '), 1)
                    self.assertEqual(query_string.count('extract'), 0)
                # an expression rhs cannot use the between optimization.
                qs = DTModel.objects.annotate(
                    start_year=ExtractYear('start_datetime'),
@@ -144,10 +156,16 @@ class DateFunctionTests(TestCase):
            with self.subTest(lookup):
                qs = DTModel.objects.filter(**{'start_datetime__%s__gt' % lookup: 2015})
                self.assertEqual(qs.count(), 1)
                if lookup == 'iso_year':
                    self.assertGreaterEqual(str(qs.query).lower().count('extract'), 1)
                else:
                    self.assertEqual(str(qs.query).lower().count('extract'), 0)
                qs = DTModel.objects.filter(**{'start_datetime__%s__gte' % lookup: 2015})
                self.assertEqual(qs.count(), 2)
                if lookup == 'iso_year':
                    self.assertGreaterEqual(str(qs.query).lower().count('extract'), 1)
                else:
                    self.assertEqual(str(qs.query).lower().count('extract'), 0)
                qs = DTModel.objects.annotate(
                    start_year=ExtractYear('start_datetime'),
                ).filter(**{'end_datetime__%s__gte' % lookup: F('start_year')})
@@ -167,10 +185,16 @@ class DateFunctionTests(TestCase):
            with self.subTest(lookup):
                qs = DTModel.objects.filter(**{'start_datetime__%s__lt' % lookup: 2016})
                self.assertEqual(qs.count(), 1)
                if lookup == 'iso_year':
                    self.assertGreaterEqual(str(qs.query).lower().count('extract'), 1)
                else:
                    self.assertEqual(str(qs.query).lower().count('extract'), 0)
                qs = DTModel.objects.filter(**{'start_datetime__%s__lte' % lookup: 2016})
                self.assertEqual(qs.count(), 2)
                if lookup == 'iso_year':
                    self.assertGreaterEqual(str(qs.query).lower().count('extract'), 1)
                else:
                    self.assertEqual(str(qs.query).lower().count('extract'), 0)
                qs = DTModel.objects.annotate(
                    end_year=ExtractYear('end_datetime'),
                ).filter(**{'start_datetime__%s__lte' % lookup: F('end_year')})