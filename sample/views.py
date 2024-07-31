from django.shortcuts import render
from .models import Movie
from rest_framework import status
from rest_framework.response import Response
from django.http import JsonResponse
from .serializers import MovieSerializer
from django.http import HttpResponse
from rest_framework.views import APIView

class moviewithserializer(APIView):
    
    def get(self,request):
        queryset = Movie.objects.all()
        serializer = MovieSerializer(queryset,many=True)
        return Response(serializer.data)
    def post(self, request, format=None):
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def home(requst):
    return HttpResponse("Hey Homelander this side! (without tailwind css)")
import json
def getmovies(request):
    # if request.method == 'GET':
    movies = Movie.objects.all()
    jsonobj={}
    data=[]
    for movie in movies:
        temp={}
        temp['name'] = movie.name
        temp['desc'] = movie.desc
        temp['img_url'] = movie.img_url
        temp['rating'] = movie.rating
        data.append(temp)
    # jsonobj = json.loads(json.dumps(jsonobj))
    jsonobj['data'] = data
    return JsonResponse(jsonobj)
    # return json_str
        # return {jsonobj: jsonobj}
    
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