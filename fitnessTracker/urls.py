from django.urls import path

from . import views

app_name = "fitnessTracker"

urlpatterns = [
    path('', views.index, name='index'),
]