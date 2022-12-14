from django.db import models

# Create your models here.
class Director(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    duration = models.IntegerField(null=True, blank=True)
    director = models.ForeignKey(Director,related_name='directors', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Review(models.Model):
    text = models.CharField(max_length=100)
    movie = models.ForeignKey(Movie, related_name='ratings', on_delete=models.CASCADE)
    rate_choices = (
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5)
    )
    stars = models.IntegerField(choices=rate_choices)

    def __str__(self):
        return self.text

