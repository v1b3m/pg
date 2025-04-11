@@ -37,6 +37,9 @@ def __str__(self):
class Book(models.Model):
    name = models.CharField(max_length=50)


class Author(models.Model):
    name = models.CharField(max_length=50)