from django.conf.urls import url
from django.http import HttpResponse
from requests import __title__
import feedparser
from django.core import serializers
from django.http import JsonResponse
from .AddData import main
from .models import NewsArticle , SportsNewsArticle , TechNewsArticle , HealthNewsArticle , ScienceNewsArticle , BusinessNewsArticle , EntertainmentNewsArticle
from django.forms.models import model_to_dict
import json
from .mrEncoder import decodeIt  

def gethomenews(request):
    #main()
    _totalNews = int(request.GET.get('totalnews', ''))
    fromNews =  _totalNews - 12 
    toNews =  _totalNews
    if(toNews != ''):
         news = list(NewsArticle.objects.order_by('-pubDate')[fromNews:toNews].values())
    else:
        news = list(NewsArticle.objects.order_by('-pubDate')[0:12].values())
    return JsonResponse(news , safe=False)


def getSpecificHomeNews(request , titleIn):
    if NewsArticle.objects.filter(shortedUrl=titleIn).exists():
        news_item = serializers.serialize('json', NewsArticle.objects.filter(shortedUrl=titleIn))
        return JsonResponse(news_item , safe=False)
    else:
        print("News not Found")
        return 404

def SearchHomeNews(searchTag):
    if NewsArticle.objects.filter(title__contains = searchTag).exists():
        news_item = serializers.serialize('json', NewsArticle.objects.filter(title__contains = searchTag))
        return JsonResponse(news_item , safe=False)
    else:
        print("News not Found")
        return 404





# Sports Section

def getsportsnews(request):
    #main()
    _totalNews = int(request.GET.get('totalnews', ''))
    fromNews =  _totalNews - 12 
    toNews =  _totalNews
    if(toNews != ''):
         news = list(SportsNewsArticle.objects.order_by('-pubDate')[fromNews:toNews].values())
    else:
        news = list(SportsNewsArticle.objects.order_by('-pubDate')[0:12].values())
    return JsonResponse(news , safe=False)

def getSpecificSportsNews(request , titleIn):
    if SportsNewsArticle.objects.filter(shortedUrl=titleIn).exists():
        news_item = serializers.serialize('json', SportsNewsArticle.objects.filter(shortedUrl=titleIn))
        return JsonResponse(news_item , safe=False)
    else:
        print("News not Found")
        return 404

# Technology News


def getTechnews(request):
    #main()
    _totalNews = int(request.GET.get('totalnews', ''))
    fromNews =  _totalNews - 12 
    toNews =  _totalNews
    if(toNews != ''):
         news = list(TechNewsArticle.objects.order_by('-pubDate')[fromNews:toNews].values())
    else:
        news = list(TechNewsArticle.objects.order_by('-pubDate')[0:12].values())
    return JsonResponse(news , safe=False)

def getSpecificTechNews(request , titleIn):
    if TechNewsArticle.objects.filter(shortedUrl=titleIn).exists():
        news_item = serializers.serialize('json', TechNewsArticle.objects.filter(shortedUrl=titleIn))
        return JsonResponse(news_item , safe=False)
    else:
        print("News not Found")
        return 404


# Health News


def getHealthnews(request):
    #main()
    _totalNews = int(request.GET.get('totalnews', ''))
    fromNews =  _totalNews - 12 
    toNews =  _totalNews
    if(toNews != ''):
         news = list(HealthNewsArticle.objects.order_by('-pubDate')[fromNews:toNews].values())
    else:
        news = list(HealthNewsArticle.objects.order_by('-pubDate')[0:12].values())
    return JsonResponse(news , safe=False)

def getSpecificHealthNews(request , titleIn):
    if HealthNewsArticle.objects.filter(shortedUrl=titleIn).exists():
        news_item = serializers.serialize('json', HealthNewsArticle.objects.filter(shortedUrl=titleIn))
        return JsonResponse(news_item , safe=False)
    else:
        print("News not Found")
        return 404

# Science News


def getSciencenews(request):
    #main()
    _totalNews = int(request.GET.get('totalnews', ''))
    fromNews =  _totalNews - 12 
    toNews =  _totalNews
    if(toNews != ''):
         news = list(ScienceNewsArticle.objects.order_by('-pubDate')[fromNews:toNews].values())
    else:
        news = list(ScienceNewsArticle.objects.order_by('-pubDate')[0:12].values())
    return JsonResponse(news , safe=False)

def getSpecificScienceNews(request , titleIn):
    if ScienceNewsArticle.objects.filter(shortedUrl=titleIn).exists():
        news_item = serializers.serialize('json', ScienceNewsArticle.objects.filter(shortedUrl=titleIn))
        return JsonResponse(news_item , safe=False)
    else:
        print("News not Found")
        return 404

# Bussiness News


def getBussinessnews(request):
    #main()
    _totalNews = int(request.GET.get('totalnews', ''))
    fromNews =  _totalNews - 12 
    toNews =  _totalNews
    if(toNews != ''):
         news = list(BusinessNewsArticle.objects.order_by('-pubDate')[fromNews:toNews].values())
    else:
        news = list(BusinessNewsArticle.objects.order_by('-pubDate')[0:12].values())
    return JsonResponse(news , safe=False)

def getSpecificBussinessNews(request , titleIn):
    if BusinessNewsArticle.objects.filter(shortedUrl=titleIn).exists():
        news_item = serializers.serialize('json', BusinessNewsArticle.objects.filter(shortedUrl=titleIn))
        return JsonResponse(news_item , safe=False)
    else:
        print("News not Found")
        return 404

# Entertainment News


def getEntertainmentnews(request):
    #main()
    _totalNews = int(request.GET.get('totalnews', ''))
    fromNews =  _totalNews - 12 
    toNews =  _totalNews
    if(toNews != ''):
         news = list(EntertainmentNewsArticle.objects.order_by('-pubDate')[fromNews:toNews].values())
    else:
        news = list(EntertainmentNewsArticle.objects.order_by('-pubDate')[0:12].values())
    return JsonResponse(news , safe=False)

def getSpecificEntertainmentNews(request , titleIn):
    if EntertainmentNewsArticle.objects.filter(shortedUrl=titleIn).exists():
        news_item = serializers.serialize('json', EntertainmentNewsArticle.objects.filter(shortedUrl=titleIn))
        return JsonResponse(news_item , safe=False)
    else:
        print("News not Found")
        return 404



def getSpecificNewsUrl(titleIn):
    if NewsArticle.objects.filter(shortedUrl=titleIn).exists():
        news_item = serializers.serialize('json', NewsArticle.objects.filter(shortedUrl=titleIn))
        res = json.loads(news_item)
        return res[0]
    elif SportsNewsArticle.objects.filter(shortedUrl=titleIn).exists():
        news_item = serializers.serialize('json', SportsNewsArticle.objects.filter(shortedUrl=titleIn))
        res = json.loads(news_item)
        return res[0]
    elif TechNewsArticle.objects.filter(shortedUrl=titleIn).exists():
        news_item = serializers.serialize('json', TechNewsArticle.objects.filter(shortedUrl=titleIn))
        res = json.loads(news_item)
        return res[0]
    elif HealthNewsArticle.objects.filter(shortedUrl=titleIn).exists():
        news_item = serializers.serialize('json', HealthNewsArticle.objects.filter(shortedUrl=titleIn))
        res = json.loads(news_item)
        return res[0]
    elif ScienceNewsArticle.objects.filter(shortedUrl=titleIn).exists():
        news_item = serializers.serialize('json', ScienceNewsArticle.objects.filter(shortedUrl=titleIn))
        res = json.loads(news_item)
        return res[0]
    elif BusinessNewsArticle.objects.filter(shortedUrl=titleIn).exists():
        news_item = serializers.serialize('json', BusinessNewsArticle.objects.filter(shortedUrl=titleIn))
        res = json.loads(news_item)
        return res[0]
    elif EntertainmentNewsArticle.objects.filter(shortedUrl=titleIn).exists():
        news_item = serializers.serialize('json', EntertainmentNewsArticle.objects.filter(shortedUrl=titleIn))
        res = json.loads(news_item)
        return res[0]    
    else:
        print("News not Found")
        return "404"