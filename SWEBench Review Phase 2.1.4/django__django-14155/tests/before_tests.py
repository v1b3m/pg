        self.assertEqual(
            repr(resolve('/no_kwargs/42/37/')),
            "ResolverMatch(func=urlpatterns_reverse.views.empty_view, "
            "args=('42', '37'), kwargs={}, url_name=no-kwargs, app_names=[], "
            "namespaces=[], route=^no_kwargs/([0-9]+)/([0-9]+)/$)",
        )


@override_settings(ROOT_URLCONF='urlpatterns_reverse.erroneous_urls')
class ErroneousViewTests(SimpleTestCase):