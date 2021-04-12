from Xtranews.models import NewsArticle , SportsNewsArticle , TechNewsArticle , HealthNewsArticle , ScienceNewsArticle , BusinessNewsArticle , EntertainmentNewsArticle
import feedparser
from Xtranews import mrEncoder
from bs4 import BeautifulSoup
import lxml
import requests as rs
from dateutil import parser

Ndtv_Categories = {
    'Top': 'http://feeds.feedburner.com/ndtvnews-top-stories?format=xml',
    'Trending': 'http://feeds.feedburner.com/ndtvnews-trending-news?format=xml',
    'Sports':'http://feeds.feedburner.com/ndtvsports-latest?format=xml',
    'Cricket':'http://feeds.feedburner.com/ndtvsports-cricket?format=xml',
    'Tech':'https://feeds.feedburner.com/gadgets360-latest',
    'Food':'https://feeds.feedburner.com/ndtvcooks-latest',
    'Entertainment':'https://feeds.feedburner.com/ndtvmovies-latest',
    'Business':'https://feeds.feedburner.com/ndtvprofit-latest',
}

def NDTV():
    #NDTV
    feed = feedparser.parse(Ndtv_Categories["Top"])
    for item in feed.entries:
        article = NewsArticle()
        if not NewsArticle.objects.filter(link=item.link).exists():
          if not NewsArticle.objects.filter(title=item.title).exists():  
            article.shortedUrl = mrEncoder.encodeTitle(item.title)
            article.title = item.title
            article.pubDate = parser.parse(item.updatedat)
            article.description = item.description
            if item.fullimage:
                article.image = item.fullimage
            else:
                break
            article.publisher = 'NDTV'
            article.link = item.link
            article.save()


    #NDTV Trending
    feed = feedparser.parse(Ndtv_Categories["Trending"])
    for item in feed.entries:
        article = NewsArticle()
        if not NewsArticle.objects.filter(link=item.link).exists():
          if not NewsArticle.objects.filter(title=item.title).exists():    
            article.shortedUrl = mrEncoder.encodeTitle(item.title)
            article.title = item.title
            article.pubDate = parser.parse(item.updatedat)
            article.description = item.description
            if item.fullimage:
                article.image = item.fullimage
            else:
                break
            article.publisher = 'NDTV'
            article.link = item.link
            article.save()
    
    # NDTV Sports

    feed = feedparser.parse(Ndtv_Categories["Sports"])
    for item in feed.entries:
        article = SportsNewsArticle()
        if not SportsNewsArticle.objects.filter(link=item.link).exists():
          if not SportsNewsArticle.objects.filter(title=item.title).exists():    
            article.shortedUrl = mrEncoder.encodeTitle(item.title)
            article.title = item.title
            article.pubDate = parser.parse(item.updatedat)
            article.description = item.description
            if item.fullimage:
                article.image = item.fullimage
            else:
                break
            article.publisher = 'NDTV'
            article.link = item.link
            article.save()

    # Cricket

    feed = feedparser.parse(Ndtv_Categories["Cricket"])
    for item in feed.entries:
        article = SportsNewsArticle()
        if not SportsNewsArticle.objects.filter(link=item.link).exists():
          if not SportsNewsArticle.objects.filter(title=item.title).exists():   
            article.shortedUrl = mrEncoder.encodeTitle(item.title)
            article.title = item.title
            article.pubDate = parser.parse(item.updatedat)
            article.description = item.description
            if item.fullimage:
                article.image = item.fullimage
            else:
                break
            article.publisher = 'NDTV'
            article.link = item.link
            article.save()

    # TEch

    feed = feedparser.parse(Ndtv_Categories["Tech"])
    for item in feed.entries:
        article = TechNewsArticle()
        if not TechNewsArticle.objects.filter(link=item.link).exists():
          if not TechNewsArticle.objects.filter(title=item.title).exists():    
            article.shortedUrl = mrEncoder.encodeTitle(item.title)
            article.title = item.title
            article.pubDate = parser.parse(item.updatedat)
            article.description = item.description
            if item.fullimage:
                article.image = item.fullimage
            else:
                break
            article.publisher = 'Gadgets360'
            article.link = item.link
            article.save()

     # Health

    feed = feedparser.parse(Ndtv_Categories["Food"])
    for item in feed.entries:
        article = HealthNewsArticle()
        if not HealthNewsArticle.objects.filter(link=item.link).exists():
          if not HealthNewsArticle.objects.filter(title=item.title).exists():    
            article.shortedUrl = mrEncoder.encodeTitle(item.title)
            article.title = item.title
            article.pubDate = parser.parse(item.updatedat)
            article.description = item.description
            if item.fullimage:
                article.image = item.fullimage
            else:
                break
            article.publisher = 'NDTV'
            article.link = item.link
            article.save()
    
    # Business 

    feed = feedparser.parse(Ndtv_Categories["Business"])
    for item in feed.entries:
        article = BusinessNewsArticle()
        if not BusinessNewsArticle.objects.filter(link=item.link).exists():
          if not BusinessNewsArticle.objects.filter(title=item.title).exists():    
            article.shortedUrl = mrEncoder.encodeTitle(item.title)
            article.title = item.title
            article.pubDate = parser.parse(item.updatedat)
            article.description = item.description
            if item.fullimage:
                article.image = item.fullimage
            else:
                break
            article.publisher = 'NDTV'
            article.link = item.link
            article.save()
    
    # Entertainment

    feed = feedparser.parse(Ndtv_Categories["Entertainment"])
    for item in feed.entries:
        article = EntertainmentNewsArticle()
        if not EntertainmentNewsArticle.objects.filter(link=item.link).exists():
          if not EntertainmentNewsArticle.objects.filter(title=item.title).exists():    
            article.shortedUrl = mrEncoder.encodeTitle(item.title)
            article.title = item.title
            article.pubDate = parser.parse(item.updatedat)
            article.description = item.description
            if item.fullimage:
                article.image = item.fullimage
            else:
                break
            article.publisher = 'NDTV'
            article.link = item.link
            article.save()
  
