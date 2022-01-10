from django.db import models


class Producten(models.Model):
    naam = models.CharField(max_length=155)
    def __str__(self):
        return self.naam
    slug = models.SlugField(max_length=155, default='')
    prijs = models.DecimalField(max_digits=6, decimal_places=2)
    actieprijs = models.DecimalField(max_digits=6, decimal_places=2)
    voorraad = models.IntegerField()
    description = models.TextField()
    afbeelding = models.TextField(max_length=2083)
    actief = models.BooleanField(default=True)



class Acties(models.Model):
    code = models.CharField(max_length=10)
    def __str__(self):
        return self.code
    beschrijving = models.CharField(max_length=255)
    korting = models.FloatField()
