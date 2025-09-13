from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Movie

def home(request):
    return HttpResponse("Welcome to the Movie Collection System!")

def movies_list(request):
    movies = Movie.objects.all()
    return render(request, 'movies.html', {'movies': movies})

def movie_detail(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    return render(request, 'movie_detail.html', {'movie': movie})