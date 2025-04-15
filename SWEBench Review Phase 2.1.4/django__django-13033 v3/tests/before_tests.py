            attrgetter("headline")
        )

    def test_order_by_f_expression(self):
        self.assertQuerysetEqual(
            Article.objects.order_by(F('headline')), [