from django.shortcuts import render
from django.http import HttpResponse

from .models import Post


def booking(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'booking/home.html', context)


def about(request):
    return render(request, 'booking/about.html', {'title': 'About'})
