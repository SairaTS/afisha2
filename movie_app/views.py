from django.db.models import Avg
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
from .models import *

# Create your views here.
@api_view(['GET'])
def director_view(request):
    directors = Director.objects.all()
    serializer = DirectortSerializer(directors, many=True)
    return Response(data=serializer.data)

@api_view(['GET'])
def director_detail_view(request, id):
    try:
        director = Director.objects.get(id=id)
    except Director.DoesNotExist:
        return Response(data={'error': 'Director not found!'})
    data = DirectortSerializer(director).data
    return Response(data=data)

@api_view(['GET'])
def movie_view(request):
    movies = Movie.objects.all()
    serializer = MovieSerializer(movies, many=True)
    return Response(data=serializer.data)

@api_view(['GET'])
def movie_detail_view(request, id):
    try:
        movie = Movie.objects.get(id=id)
    except Movie.DoesNotExist:
        return Response(data={'error:' 'Movie not found!'})
    data = MovieSerializer(movie).data
    return Response(data=data)

@api_view(['GET'])
def review_view(request):
    reviews = Review.objects.all()
    serializer = ReviewSerializer(reviews, many=True)
    return Response(data=serializer.data)

@api_view(['GET'])
def review_detail_view(request, id):
    try:
        review = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(data={'error:' 'Review not found!'})
    data = ReviewSerializer(review).data
    return Response(data=data)


@api_view(['GET'])
def avg_reviews(request):
    movies = Movie.objects.annotate(
        average_rating=models.Sum(models.F('ratings')) / models.Count(models.F('ratings'))
    )
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def film_directors(request):
    directors = Movie.objects.annotate(count_of_movies=models.Sum(models.F('director')))
    serializer = MoviesDirectors(directors, many=True)
    return Response(serializer.data)
