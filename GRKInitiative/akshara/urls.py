from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views


urlpatterns = [
    path('', views.homepage, name="home"),
    path('letters/', views.viewletters, name="letters"),
    path('words4letter/', views.words4letterpage, name="words4letter"),
    path('randomletter/', views.randomletter, name="randomletter"),
    path('randomletters/', views.randomletters, name="randomletters"),
    path('randomengword/', views.random_eng_word, name="randomengword"),
    path('randomkanword/', views.random_kan_word, name="randomkanword"),
    path('randomimage/', views.random_image, name="randomimage"),


]
