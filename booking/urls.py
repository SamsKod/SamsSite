from django.urls import path
from . import views

urlpatterns = [
    path('', views.booking, name='booking-home'),
    path('about/', views.about, name='booking-about'),
]
