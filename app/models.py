from django.db import models

# Create your models here.
class Movie(models.Model):
    movie_name=models.CharField(max_length=100,primary_key=True)

    def __str__(self):
        return self.movie_name

class Details(models.Model):
    movie_name=models.ForeignKey(Movie,on_delete=models.CASCADE)
    hero_name=models.CharField(max_length=100)
    director=models.CharField(max_length=100)

    def __str__(self):
        return self.hero_name

class Hero_details(models.Model):
    hero_name=models.ForeignKey(Details,on_delete=models.CASCADE)
    status=models.CharField(max_length=100)

    def __str__(self):
        return self.status
