from django.urls import path
from django.shortcuts import render
from . import views

urlpatterns = [
    path('20-raisons/', views.article_20_raisons, name='20-raisons'),
    path('bienfaits-sport/', views.article_bienfaits_sport, name='bienfaits-sport'),
    path('conseils-debutant/', views.article_conseils_debutant, name='conseils-debutant'),
    path('rester-motive/', views.article_rester_motive, name='rester-motive'),
    path('bruler-calories/', views.article_bruler_calories, name='bruler-calories'),
    path('etirements/', views.article_etirements, name='etirements'),
    path('search/', views.search, name='search'),

]
