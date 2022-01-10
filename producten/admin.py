from django.contrib import admin
from . models import Producten, Acties


class ProductenAdmin(admin.ModelAdmin):
    list_display = ('naam', 'prijs', 'actieprijs', 'voorraad')


class ActiesAdmin(admin.ModelAdmin):
    list_display = ('code', 'beschrijving', 'korting')


admin.site.register(Producten, ProductenAdmin)
admin.site.register(Acties, ActiesAdmin)
