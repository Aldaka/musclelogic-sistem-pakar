from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('konsultasi/', views.form_konsultasi, name='form_konsultasi'),
]