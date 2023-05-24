from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from app.models import *
def hero(request):
    m=input('enter the movie name: ')
    mo=Movie.objects.get_or_create(movie_name=m)[0]
    mo.save()
    return HttpResponse('data inserted successfully')
def name(request):
    m=input('enter the movie name: ')
    hn=input('enter hero name: ')
    d=input('enter director nmae: ')
    mo=Movie.objects.get_or_create(movie_name=m)[0]
    do=Details.objects.get_or_create(movie_name=mo,hero_name=hn,director=d)[0]
    do.save()
    return HttpResponse('data inserted successfully')
def hd(request):
    m=input('enter the movie name: ')
    hn=input('enter hero name: ')
    d=input('enter director nmae: ')
    s=input('enter marriage status: ')
    mo=Movie.objects.get_or_create(movie_name=m)[0]
    do=Details.objects.get_or_create(movie_name=mo,hero_name=hn,director=d)[0]
    hd=Hero_details.objects.get_or_create(hero_name=do,status=s)[0]
    hd.save()
    return HttpResponse('data inserted successfully')
    