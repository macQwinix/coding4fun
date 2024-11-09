from django.contrib import admin
from django.urls import path, include
from mac.views import home, about

urlpatterns = [
    path('', home, name='home'),
    path('about', about, name='about'),

]
