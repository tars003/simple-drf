from django.db import models


class Categories(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Articles(models.Model):
    link = models.CharField(max_length=500)
    categories = models.ManyToManyField(Categories)
    rating = models.FloatField()

    def __str__(self):
        return self.link
