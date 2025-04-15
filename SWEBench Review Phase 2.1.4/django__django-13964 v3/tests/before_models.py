    bestchild = models.ForeignKey('Child', models.SET_NULL, null=True, related_name='favored_by')


class Child(models.Model):
    name = models.CharField(max_length=20)
    parent = models.ForeignKey(Parent, models.CASCADE)
    parent = models.ForeignKey(Parent, models.CASCADE, null=True)


class ToFieldChild(models.Model):
    parent = models.ForeignKey(Parent, models.CASCADE, to_field='name', related_name='to_field_children')
