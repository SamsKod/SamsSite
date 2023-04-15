from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'booking/home.html', {'title': 'Bookings'})


def about(request):
    return render(request, 'booking/about.html', {'title': 'About'})
