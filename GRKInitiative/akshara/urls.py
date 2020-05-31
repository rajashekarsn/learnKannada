from django.urls import path
from . import views


urlpatterns = [
    path('', views.homepage, name="home"),
    path('letters/', views.viewletters, name="letters"),
    path('randomletter/', views.randomletter, name="randomletter"),
    path('randomletters/', views.randomletters, name="randomletters"),
]
