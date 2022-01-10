from django.db import models

class Blog(models.Model):
    naam = models.CharField(max_length=155)
    def __str__(self):
        return self.naam
    slug = models.SlugField(max_length=155)
    afbeelding = models.ImageField()
    omschrijving = models.TextField()
    datum = models.DateTimeField()


