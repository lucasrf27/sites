from django.shortcuts import render
from .models import Experiencias


def HomeView(request):
    queryset = Experiencias.objects.all()
    return render(request, 'experiences.html', {'queryset': queryset})
