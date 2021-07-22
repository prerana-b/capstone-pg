from django.shortcuts import render
# Create your views here.
from .models import Postproperty


def home(request):
    context = {
        'posts': Postproperty.objects.all()
    }
    return render(request, 'properties/home.html', context)


def about(request):
    return render(request, 'properties/about.html', {'title': 'About'})
