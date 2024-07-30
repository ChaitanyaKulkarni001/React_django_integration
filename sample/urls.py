
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home),
    path('seemovie/',views.seemovie,name='seemovie'),
    path('addmovie/',views.addMovie,name='addMovie'),
]