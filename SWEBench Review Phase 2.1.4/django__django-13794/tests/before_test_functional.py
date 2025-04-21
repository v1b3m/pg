        with self.assertRaisesMessage(TypeError, msg):
            Foo().cp

    def test_lazy_equality(self):
        """
        == and != work correctly for Promises.