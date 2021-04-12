from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
import feedparser
from .getnews import SearchHomeNews
from .mrEncoder import decodeIt 
from bs4 import BeautifulSoup
import requests as rs

# Create your views here.

def redirectToHome(request):
    response = redirect('/home')
    return response

def homepage(request , title=''):
    if not request.GET.get('search', ''):
        if(title):
            context = {
                'realnews' : title ,
                'category' : 'home',
            }
            return render(request , 'categories/homepage.html', context)
        else:
            context = {
                'category' : 'home',
            }
            return render(request , 'categories/homepage.html', context )
    else:
        searchTag = str(request.GET.get('search', ''))
        context = {
                'realnews' : title ,
                'category' : 'home',
            }
        return SearchHomeNews(searchTag)


def sports(request, title=''):
    if(title):
        context = {
            'realnews' : title ,
            'category' : 'sports',
        }
        return render(request , 'categories/sports.html', {'realnews' : title })
    else:
        context = {
            'category' : 'sports',
        }
        return render(request , 'categories/sports.html', context)

def tech(request, title=''):
    if(title):
        context = {
            'realnews' : title ,
            'category' : 'tech',
        }
        return render(request , 'categories/technology.html', context)
    else:
        context = {
            'category' : 'tech',
        }
        return render(request , 'categories/technology.html', context)

def health(request, title=''):
    if(title):
        context = {
            'realnews' : title ,
            'category' : 'health',
        }
        return render(request , 'categories/health.html', context)
    else:
        context = {
            'category' : 'health',
        }
        return render(request , 'categories/health.html', context)

def science(request, title=''):
    if(title):
        context = {
            'realnews' : title ,
            'category' : 'science',
        }
        return render(request , 'categories/science.html', context)
    else:
        context = {
            'category' : 'science',
        }
        return render(request , 'categories/science.html', context)

def bussiness(request, title=''):
    if(title):
        context = {
            'realnews' : title ,
            'category' : 'business',
        }
        return render(request , 'categories/business.html',context)
    else:
        context = {
            'category' : 'business',
        }
        return render(request , 'categories/business.html', context)

def entertainment(request, title=''):
    if(title):
        context = {
            'realnews' : title ,
            'category' : 'entertainment',
        }
        return render(request , 'categories/entertainment.html',context)
    else:
        context = {
            'category' : 'entertainment',
        }
        return render(request , 'categories/entertainment.html', context)