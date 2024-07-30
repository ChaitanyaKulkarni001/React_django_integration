from django.shortcuts import render
from .models import Movie
# Create your views here.

from django.http import HttpResponse

def home(requst):
    return HttpResponse("Hey Homelander this side! (without tailwind css)")

def seemovie(request):
    if request.method == 'GET':
        movies = Movie.objects.all()
        print(movies)
        return render(request, 'seemovie.html', {'movies': movies})
    if request.method == 'POST':
        # print(requst)
        name = request.POST.get('name')
        desc = request.POST.get('desc')
        img_url = request.POST.get('img_url')
        rating = request.POST.get('rating')
        
        new_movie = Movie(name=name,desc=desc,img_url=img_url,rating=rating)
        new_movie.save()   
        movies = Movie.objects.all()
        return render(request, 'seemovie.html', {'movies': movies})

def addMovie(request):
    return render(request, 'addMovie.html')