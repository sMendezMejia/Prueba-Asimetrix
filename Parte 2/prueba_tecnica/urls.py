from django.contrib import admin
from django.urls import path

from pollos import views as pollos_views

urlpatterns = [
    path('', pollos_views.pollos_api),
]
