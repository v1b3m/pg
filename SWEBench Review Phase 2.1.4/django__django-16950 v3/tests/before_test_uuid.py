            }
        )
        self.assertTrue(formset.is_valid())

    def test_inlineformset_factory_nulls_default_pks_uuid_parent_auto_child(self):
        """
        )
        formset = FormSet()
        self.assertIsNone(formset.forms[0].fields["parent"].initial)