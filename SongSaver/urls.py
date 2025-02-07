
from django.urls import path
from . import views

urlpatterns = [
    path('', views.startup_page, name='Loader'),
    path('/dashboard', views.dashboard_page, name='Dashboard'),
    path('/list', views.listing_page, name='Tracks'),
]