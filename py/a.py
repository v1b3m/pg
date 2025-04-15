with transaction.atomic():
    order = Order()
    order.product = Product(sku="foo")
    order.product.save()
    order.save()
    assert Order.objects.filter(product=order.product).exists()  # succeeds
