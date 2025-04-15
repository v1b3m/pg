
class Author(models.Model):
    name = models.CharField(max_length=63, null=True, blank=True)

    class Meta:
        ordering = ('-pk',)