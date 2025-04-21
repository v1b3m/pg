@@ -2,6 +2,7 @@ from datetime import date, timedelta

from django.template.defaultfilters import add
from django.test import SimpleTestCase
from django.utils.translation import gettext_lazy

from ..utils import setup

@@ -46,6 +47,11 @@ class AddTests(SimpleTestCase):
        output = self.engine.render_to_string('add07', {'d': date(2000, 1, 1), 't': timedelta(10)})
        self.assertEqual(output, 'Jan. 11, 2000')

    @setup({'add_lazy': '{{ s1|add:s2 }}'})
    def test_add_lazy(self):
        output = self.engine.render_to_string('add_lazy', {'s1': 'foo', 's2': gettext_lazy('bar')})
        self.assertEqual(output, 'foobar')


class FunctionTests(SimpleTestCase):
