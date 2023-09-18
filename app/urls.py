from django.urls import path
from . import views

urlpatterns = [
    path('scrape/', views.scrape_properties, name='scrape_properties'),
]
