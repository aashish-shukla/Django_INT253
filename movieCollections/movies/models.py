from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=200)
    director = models.CharField(max_length=100)
    release_year = models.PositiveIntegerField()
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.title