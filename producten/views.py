from django.http import HttpResponse
from django.shortcuts import render
from .models import Producten
from django.shortcuts import get_object_or_404


def index(request):
    products = Producten.objects.all()
    return render(request, './producten.html', {'products' : products})


def nieuw(request):
    return HttpResponse('Nieuwe producten!')


def detail(request, id, slug):
    product = get_object_or_404(Producten, id=id)
    context = {'product': product}
    return render(request, './detail.html', context)


