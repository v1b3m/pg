@@ -18,6 +18,7 @@

class Author(models.Model):
    name = models.CharField(max_length=63, null=True, blank=True)
    editor = models.ForeignKey('self', models.CASCADE, null=True)

    class Meta:
        ordering = ('-pk',)