
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home),
    path('seemovie/',views.seemovie,name='seemovie'),
    path('addmovie/',views.addMovie,name='addMovie'),
    path('api/getmovies/',views.getmovies,name='getmovies'), 
    path('api/moviewithserializer/',views.moviewithserializer.as_view(),name='moviewithserializer'),
]