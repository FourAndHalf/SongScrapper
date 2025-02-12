#region Declarations

from django.urls import path
from . import views

#endregion

#region Web URLs

urlpatterns = [
    path('', views.startup_page, name='Loader'),
    path('pre_dashboard', views.pre_dashboard_page, name='Pre-Dashboard'),
    path('dashboard', views.dashboard_page, name='Dashboard'),
    path('list', views.listing_page, name='Tracks'),
    path('fav_list', views.fav_listing_page, name='Ranked'),
    path('create_link', views.create_link_page, name="Link"),
]

#endregion