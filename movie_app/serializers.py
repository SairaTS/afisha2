from rest_framework import serializers
from .models import *

class DirectortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = '__all__'

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    movie = MovieSerializer()
    class Meta:
        model = Review
        fields = '__all__'



class MovieListSerializer(serializers.ModelSerializer):
    average_rating = serializers.FloatField()

    class Meta:
        model = Movie
        fields = ("id", "title", "average_rating")

class MoviesDirectors(serializers.ModelSerializer):
    count_of_movies = serializers.IntegerField()
    # director = DirectortSerializer()
    class Meta:
        model=Director
        fields=("id", "count_of_movies")

