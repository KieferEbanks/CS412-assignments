# File: urls.py
# Author: Kiefer Ebanks (kebanks@bu.edu), 1/27/20026
# Description: The URL file for the quotes app
# Creating the URLs for the quotes app


from django.urls import path
from django.conf import settings
from . import views
 
# Creating my URLs. So far just the home page.
urlpatterns = [ 
    path(r'', views.home, name="home"),
    path(r'quote/', views.quote, name="quote"),
    path(r'show_all/', views.show_all, name="show_all"),
    path(r'about/', views.about, name="about"),
]