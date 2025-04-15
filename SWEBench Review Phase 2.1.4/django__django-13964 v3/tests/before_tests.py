from django.utils.translation import gettext_lazy

from .models import (
    Article, Category, Child, ChildNullableParent, City, Country, District,
    First, Parent, Record, Relation, Reporter, School, Student, Third,
    ToFieldChild,
)


        self.assertEqual(child.parent, parent)
        self.assertEqual(child.parent_id, parent.name)

    def test_fk_to_bigautofield(self):
        ch = City.objects.create(name='Chicago')
        District.objects.create(city=ch, name='Far South')