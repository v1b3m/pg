    username = models.CharField(max_length=100)
    last_action = models.DateTimeField()


class StumpJoke(models.Model):
    most_recently_fooled = models.ForeignKey(