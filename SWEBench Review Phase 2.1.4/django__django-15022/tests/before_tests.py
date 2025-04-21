    DynamicListDisplayLinksChildAdmin, DynamicListFilterChildAdmin,
    DynamicSearchFieldsChildAdmin, EmptyValueChildAdmin, EventAdmin,
    FilteredChildAdmin, GroupAdmin, InvitationAdmin,
    NoListDisplayLinksParentAdmin, ParentAdmin, QuartetAdmin, SwallowAdmin,
    site as custom_site,
)
from .models import (
    Band, CharPK, Child, ChordsBand, ChordsMusician, Concert, CustomIdUser,
        cl = ia.get_changelist_instance(request)
        self.assertEqual(cl.queryset.query.select_related, {'player': {}, 'band': {}})

    def test_result_list_empty_changelist_value(self):
        """
        Regression test for #14982: EMPTY_CHANGELIST_VALUE should be honored
            ('Finlayson', 1),
            ('Finlayson Hype', 0),
            ('Jonathan Finlayson Duo', 1),
            ('Mary Jonathan Duo', 1),
            ('Oscar Finlayson Duo', 0),
        ):
            with self.subTest(search_string=search_string):