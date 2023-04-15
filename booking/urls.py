from django.urls import path
from . import views
from .views import (
    PostListView,
)
urlpatterns = [
    path('', PostListView.as_view(), name='booking-home'),
    path('about/', views.about, name='booking-about'),
]
