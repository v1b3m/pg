        self.assertNoOutput(err)
        self.assertEqual(out.strip(), "Set foo")


class UtilsTests(SimpleTestCase):
    def test_no_existent_external_program(self):