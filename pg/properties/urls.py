from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='properties-home'),
    path('about/', views.about, name='properties-about'),
]
