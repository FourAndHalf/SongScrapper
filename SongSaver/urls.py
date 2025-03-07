#region Declarations

from django.urls import path
from django.contrib.sitemaps import Sitemap
from django.contrib.sitemaps.views import sitemap
from django.urls import reverse
from . import views

# Custom Sitemap class
class StaticSitemap(Sitemap):
    protocol = 'https'
    
    def items(self):
        return ['Loader', 'Dashboard', 'Tracks', 'Ranked', 'Link']
    
    def location(self, item):
        return reverse(item)
    
    def changefreq(self, item):
        if item in ['Tracks', 'Ranked']:
            return 'daily'
        return 'weekly'
    
    def priority(self, item):
        priorities = {
            'Loader': 1.0,
            'Dashboard': 0.9,
            'Tracks': 0.8,
            'Ranked': 0.8,
            'Link': 0.7
        }
        return priorities[item]

#endregion

#region Web URLs

urlpatterns = [
    path('', views.startup_page, name='Loader'),
    path('dashboard', views.dashboard_page, name='Dashboard'),
    path('list', views.listing_page, name='Tracks'),
    path('fav_list', views.fav_listing_page, name='Ranked'),
    path('create_link', views.create_link_page, name="Link"),
    
    # Sitemap URL
    path('sitemap.xml', sitemap, {'sitemaps': {'static': StaticSitemap()}},
         name='django.contrib.sitemaps.views.sitemap'),
]

#endregion