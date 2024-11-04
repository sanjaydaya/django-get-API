from django.urls import path
from . import views

urlpatterns = [
    path('vo/', views.ok, name='ok'),  # Ensure this matches the view name
    path('', views.home, name='home'),  # Ensure this matches the view name
]

