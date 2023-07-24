from django.urls import path
from . import views

urlpatterns = [
    path('link/', views.link, name='link'),
    path('datasaved/', views.link_saved_data, name='success'),
]
