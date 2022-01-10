from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('<int:id>/<slug:slug>', views.detail),
    path('nieuw', views.nieuw)
]